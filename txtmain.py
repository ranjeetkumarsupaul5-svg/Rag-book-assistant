from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatMistralAI(model = "mistral-small-2506")

data=TextLoader("document loaders/notes.txt"
)
docs=data.load()

template = ChatPromptTemplate([
    ("system","you are a AI so that summerize the text"),
    ("human","{data}")
    ])

prompt = template.format_messages(data=docs[0].page_content)


result = model.invoke(prompt)

print(result.content)