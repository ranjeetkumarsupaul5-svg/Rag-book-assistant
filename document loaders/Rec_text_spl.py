from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data=PyPDFLoader("document loaders/GNU.pdf")

docs=data.load()
splitter=RecursiveCharacterTextSplitter(#The default list is ["\n\n", "\n", " ", ""] priority order pe
    chunk_size=1000,
    chunk_overlap=10
)

chunks=splitter.split_documents(docs)
print(chunks[0].page_content)