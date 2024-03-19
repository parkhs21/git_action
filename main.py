import dotenv
import os
from langchain_openai import ChatOpenAI

# dotenv.load_dotenv()

print("TEST")
print(os.environ("COMMENT"))
print("TEST")

llm = ChatOpenAI()
chat = llm.invoke("Do you know what TmaxSoft is? Answers should be in Korean.")
# chat = "Test Answer."

with open("answer.adoc", "w") as file:
    file.write(chat.content)