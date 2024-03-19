import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
# chat = llm.invoke("Do you know what TmaxSoft is? Answers should be in Korean.")

print(os.environ["EVENT_TYPE"])

if os.environ["EVENT_TYPE"] == "issue_comment":
    chat = llm.invoke(os.environ["COMMENT"])
    chat = chat.content
    command = '"::set-output name=result::' + chat + '"'
    os.system('echo ' + command)
else:
    chat = "Test Answer about PR."

print(chat)
with open("answer.adoc", "w") as file:
    file.write(chat)