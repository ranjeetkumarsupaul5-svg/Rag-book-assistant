from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings

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
    docs,
    embeddings
)

similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("Similarity Retriever Results:")

similarity_docs = similarity_retriever.invoke(
    "What is gradient descent?"
)

for doc in similarity_docs:
    print(doc.page_content)


mmr_retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}
)

print("\nMMR Retriever Results:")

mmr_docs = mmr_retriever.invoke(
    "What is gradient descent?"
)

for doc in mmr_docs:
    print(doc.page_content)