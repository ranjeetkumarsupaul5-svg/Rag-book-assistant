from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from werkzeug.utils import secure_filename
import os
import uuid

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

embedding_model = MistralAIEmbeddings()

retriever = None
current_book = None


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """you are a helpful AI assistant.

Use only the provided information to answer the question.

If the answer is not present in the context, say:
I'm sorry, I cannot provide an answer based on the given context."""
    ),
    (
        "human",
        """context: {context}

question: {question}"""
    )
])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global retriever
    global current_book

    if "file" not in request.files:
        return jsonify({
            "message": "No file selected."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "message": "Please select a PDF."
        }), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({
            "message": "Only PDF files are allowed."
        }), 400

    try:

        filename = secure_filename(file.filename)

        upload_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(upload_path)

        print(f"Book uploaded: {filename}")

        loader = PyPDFLoader(upload_path)

        docs = loader.load()

        print(f"Pages loaded: {len(docs)}")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(docs)

        print(f"Chunks created: {len(chunks)}")

        db_path = os.path.join(
            "chroma_uploads",
            str(uuid.uuid4())
        )

        os.makedirs(db_path, exist_ok=True)

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=db_path
        )

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.5
            }
        )

        current_book = filename

        return jsonify({
            "message": "Book uploaded successfully!",
            "filename": filename,
            "pages": len(docs),
            "chunks": len(chunks)
        })

    except Exception as e:

        print("Upload error:", e)

        return jsonify({
            "message": f"Error: {str(e)}"
        }), 500


@app.route("/ask", methods=["POST"])
def ask():

    if retriever is None:
        return jsonify({
            "answer": "Please upload a PDF book first."
        })

    data = request.get_json()

    query = data.get("question", "").strip()

    if not query:
        return jsonify({
            "answer": "Please enter a question."
        })

    try:

        docs = retriever.invoke(query)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        response = llm.invoke(final_prompt)

        return jsonify({
            "answer": response.content
        })

    except Exception as e:

        return jsonify({
            "answer": f"Error: {str(e)}"
        }), 500


if __name__ == "__main__":

    print("RAG web application started successfully!")
    print("Open http://127.0.0.1:5000 in your browser")

    app.run(debug=True)