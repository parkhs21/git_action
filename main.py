import dotenv
import os
from langchain_openai import ChatOpenAI

# dotenv.load_dotenv()

# llm = ChatOpenAI()
# chat = llm.invoke("Do you know what TmaxSoft is? Answers should be in Korean.")

print(os.environ["EVENT_TYPE"])

if os.environ["EVENT_TYPE"] is "issue_comment":
    chat = "Test Answer about Comment."
else:
    chat = "Test Answer about PR."

print(chat)
with open("answer.adoc", "w") as file:
    file.write(chat)