# pip install langchain langchain-openai

import os
from getpass import getpass

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# Set API key
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")


# Calculator
@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    allowed_chars = set("0123456789+-*/(). ")

    if not all(char in allowed_chars for char in expression):
        return "Invalid mathematical expression."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except (SyntaxError, ZeroDivisionError):
        return "Could not calculate the expression."


# Word counter
@tool
def word_counter(text: str) -> str:
    """Count the number of words in a text."""
    return str(len(text.split()))


# Toolkit: collection of tools
tools = [calculator, word_counter]


# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)


# Ask the model to select a tool
question = input(
    "Ask for a calculation or word count: "
)

response = llm_with_tools.invoke(question)

# Execute the selected tool
if response.tool_calls:
    for tool_call in response.tool_calls:
        selected_tool = next(
            tool for tool in tools
            if tool.name == tool_call["name"]
        )

        result = selected_tool.invoke(tool_call["args"])

        print(f"\nTool selected: {selected_tool.name}")
        print(f"Tool result: {result}")
else:
    print("\nModel response:")
    print(response.content)