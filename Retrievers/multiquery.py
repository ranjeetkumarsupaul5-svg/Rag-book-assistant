from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(
        page_content="Gradient descent is an optimization algorithm used to minimize the loss function in machine learning models."
    ),
    Document(
        page_content="Gradient descent is an optimal algorithm used to minimize the loss function in machine learning models."
    ),
    Document(
        page_content="Neural networks use gradient descent for training."
    ),
    Document(
        page_content="Gradient descent is used in deep learning for training neural networks."
    ),
    Document(
        page_content="Gradient descent is commonly used in machine learning, especially in linear regression and logistic regression."
    )
]

embeddings = MistralAIEmbeddings()

vectorstore = Chroma.from_documents(
    docs,embeddings
)

retriever = vectorstore.as_retriever()

llm=ChatMistralAI(model="mistral-small-2506")

multi_query_retriever = MultiQueryRetriever.from_llm(
    llm=llm,
    retriever=retriever,
   
)
query = "What is gradient descent?"

multi_query_docs = multi_query_retriever.invoke(query)

print("\nMulti-Query Retriever Results:\n")
for doc in multi_query_docs:
    print(doc.page_content)


