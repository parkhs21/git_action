import dotenv
import os
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI()
chat = llm.invoke("Do you know what TmaxSoft is? Answers should be in Korean.")

os.environ["GITHUB_OUTPUT"]["result"] = chat
print(chat)