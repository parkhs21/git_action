import os
from langchain_openai import ChatOpenAI


llm = ChatOpenAI()


prompt = lambda code: f'''
Our purpose is to create a user manual for the entire program.

In the meantime, let's create a table of contents. The table of contents is the most important bone of the manual.
Since this manual is for the user, not the developer, it should be organized around the screens that will be configured.

Let's create a large table of contents with the following code.
Let’s think step by step.

##### Below Code #####
{code}
'''.strip()



if os.environ["EVENT_TYPE"] == "issue_comment":
    chat = llm.invoke(os.environ["COMMENT"])
    
else:
    with open("./src/org/yccheok/jstock/gui/OptionsJPanel.java") as file:
        content = file.read()
    chat = llm.invoke(prompt(content))



command = '"::set-output name=result::' + chat + '"'
os.system('echo ' + command)


print(chat)
with open("answer.adoc", "w") as file:
    file.write(chat.content)