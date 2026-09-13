from langchain_community.document_loaders import WebBaseLoader

url="https://www.lenovo.com/in/en/d/deals/?sortBy=priceUp&visibleDatas=4353%3ALaptops%3B4374%3AAll%2520Intel%25C2%25AE%2520Processors&cid=in:sem:3vtp7d&gad_source=1&gad_campaignid=20322680538&gbraid=0AAAAADP-YoPTUBn2NT-L4U9jOh8sCBzXH&gclid=Cj0KCQjwhsrUBhDxARIsAN3AQSeov0MXSN_b2EPbFKA3-u3RAUR2bo1U_OPjuQbYSgDwio-tcYRKdq8aAlIIEALw_wcB"

data=WebBaseLoader(url)

docs=data.load()

print(docs[0].page_content)