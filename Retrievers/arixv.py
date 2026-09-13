from langchain_community.retrievers import ArxivRetriever

arxiv_retriever = ArxivRetriever(
    load_max_docs=3
)

docs = arxiv_retriever.invoke("large language model")

for i, doc in enumerate(docs, 1):
    print(f"\nResult {i}:")
    print("Title:", doc.metadata.get("title"))
    print("Authors:", doc.metadata.get("authors"))
    print("Summary:", doc.page_content[:500])