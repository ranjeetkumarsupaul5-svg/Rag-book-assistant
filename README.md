# 📚 RAG Book Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload a PDF book and ask questions directly from its content.

The application retrieves relevant information from the uploaded book and uses an AI model to generate answers based only on the retrieved context.

---

## ✨ Features

- 📖 Upload any PDF book
- 🔍 Automatically extract and split PDF content
- 🧠 Generate embeddings using Mistral AI
- 🗄️ Store document embeddings using ChromaDB
- 🔎 Semantic document retrieval using MMR
- 🤖 Generate answers using Groq LLM
- 💬 Interactive chat-based UI
- ⚡ Flask backend
- 🌐 Ready for cloud deployment

---

## 🏗️ How It Works

```text
        📕 PDF Book
             │
             ▼
      📄 PDF Loader
             │
             ▼
       ✂️ Text Splitter
             │
             ▼
     🧠 Mistral Embeddings
             │
             ▼
        🗄️ ChromaDB
             │
             ▼
       🔎 MMR Retriever
             │
             ▼
        🤖 Groq LLM
             │
             ▼
        💬 AI Answer


🛠️ Tech Stack
Technology	Purpose
Python	Backend programming
Flask	Web application framework
LangChain	RAG pipeline
Mistral AI	Text embeddings
ChromaDB	Vector database
Groq	LLM inference
HTML	Frontend
CSS	UI design
JavaScript	Frontend interaction
📂 Project Structure
Rag-book-assistant/
│
├── app.py
├── create_database.py
├── pdfmain.py
├── txtmain.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── Retrievers/
│   ├── arixv.py
│   ├── mmr.py
│   └── multiquery.py
│
├── vector store/
│   └── DB.py
│
└── document loaders/
🚀 Run Locally
1. Clone the Repository
git clone https://github.com/ranjeetkumarsupaul5-svg/Rag-book-assistant.git
2. Open the Project
cd Rag-book-assistant
3. Create a Virtual Environment
python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure API Keys

Create a .env file in the project root:

MISTRAL_API_KEY=your_mistral_api_key
GROQ_API_KEY=your_groq_api_key

⚠️ Never upload your .env file or API keys to GitHub.

6. Start the Application
python app.py

Open:

http://127.0.0.1:5000
💡 How to Use
Open the RAG Book Assistant.
Select a PDF book.
Click Upload PDF.
Wait for the document to be processed.
Ask questions about the uploaded book.
The system retrieves relevant information from the book.
Groq generates the final answer using the retrieved context.
🔐 Environment Variables

The application requires:

MISTRAL_API_KEY
GROQ_API_KEY

For local development, store them inside a .env file.

For deployment, configure them directly in the hosting platform's environment variables.

☁️ Deployment

This project can be deployed using Render.

Production start command:

gunicorn app:app
⚠️ Important Note

The application processes uploaded PDF files and creates vector embeddings dynamically.

For production deployment, persistent storage should be configured if uploaded books and generated vector databases need to survive service restarts or redeployments.

🔮 Future Improvements
📚 Multiple book support
💾 Persistent vector storage
📝 Chat history
📄 Show source pages for answers
👤 User authentication
🌙 Dark mode
🎤 Voice-based questions
📊 Document management dashboard
⚡ Streaming AI responses
👨‍💻 Author
Ranjeet Kumar

An AI/RAG project built using:

LangChain + Mistral AI + ChromaDB + Groq + Flask

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

🌐 Live Demo

🚀 Coming soon — deployed on Render.
