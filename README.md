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
