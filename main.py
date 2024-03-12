import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI()
chat = llm.invoke("how can langsmith help with testing?, answer in korean")

print(chat)