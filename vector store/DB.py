from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(
        page_content="Python is widely used in Artificial Intelligence.",
        metadata={"source": "python.txt"}),

    Document(
        page_content="Pandas is used for data analysis in Python.",
        metadata={"source": "pandas.txt"}
    ),

    Document(
        page_content="Neural networks are used in deep learning.",
        metadata={"source": "deep_learning.txt"}
    )
]

embeddings_model = MistralAIEmbeddings()

vectorstore= Chroma.from_documents(
    documents=docs,
    embedding=embeddings_model,
    persist_directory="chroma_db"
)

result=vectorstore.similarity_search("what is used for Ml?",k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver=vectorstore.as_retriever()

docs=retriver.invoke("Explain deep learnig?")

for d in docs:
    print(d.page_content)




