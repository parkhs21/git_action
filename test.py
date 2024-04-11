from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

llm = ChatOpenAI()

class MainContents(BaseModel):
    "This is the main table of contents for the User manual."
    "The main table of contents is an important framework for the entire manual."
    "In the meantime, let's create a table of contents. The table of contents is the most important bone of the manual."
    "Since this manual is for the user, not the developer, it should be organized around the screens that will be configured."
    "Let's create a large table of contents with the following code."

    contents_name: List[str] = Field(
        ..., description="Only saves names as they appear on the Graphic in table of contents order. What the user will see, not the developer."
    )
    class_name: List[str] = Field(
        ..., description="Save the names of the calling objects in the table of contents."
    )
    

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are the team leader of a user manual production team."
            "Extract only the main table of contents from the given code."
            "The user manual is never what the developer sees. You should organize the manual by utilizing user interaction elements such as buttons."
            "Remove phrases and endings that seem to have been used during development."
            "Let's think step by step"
        ),
        ("human", "{code}"),
    ]
)

runnable = prompt | llm.with_structured_output(schema=MainContents)

with open("./src/org/yccheok/jstock/gui/OptionsJPanel.java") as file:
    code = file.read()
    
code = "##### The Given Code #####\n" + code
result = runnable.invoke({"code": code})

print(result)



# main_index_prompt = lambda code: f'''
# Our purpose is to create a user manual for the entire program.

# In the meantime, let's create a table of contents. The table of contents is the most important bone of the manual.
# Since this manual is for the user, not the developer, it should be organized around the screens that will be configured.

# Let's create a large table of contents with the following code.
# Let’s think step by step.

# ##### Below Code #####
# {code}
# '''.strip()

# temp_main_index = '''
# 1. Broker Options
# 2. Wealth Advisor Options
# 3. Alert Options
# 4. GUI Options
# 5. Speed Options
# 6. Color Options
# 7. Network Options
# 8. Indicator Options
# 9. Update Options
# '''.strip()

# detail_index_prompt = lambda code: f'''
# Our purpose is to create a user manual for the entire program.

# In the meantime, let's create a table of contents. The table of contents is the most important bone of the manual.
# Since this manual is for the user, not the developer, it should be organized around the screens that will be configured.

# ##### Main Index #####
# {temp_main_index}

# A large table of contents is shown above.

# About this indexs, we make 

# Within this table of contents, we are going to create one sub-table of contents that is most relevant.
# Let's look at the following code and think about how to create it step by step.

# ##### Below Code #####
# {code}
# '''.strip()


# def main_index():        
#     with open("./src/org/yccheok/jstock/gui/OptionsJPanel.java") as file:
#         content = file.read()
#     chat = llm.invoke(main_index_prompt(content))
#     print(chat.content)
    
# def detail_index():
#     with open("./src/org/yccheok/jstock/gui/OptionsBrokerJPanel.java") as file:
#         content = file.read()
#     chat = llm.invoke(detail_index_prompt(content))
#     print(chat.content) 
    
    
# if __name__ == "__main__":
#     detail_index()