# pip install langchain langchain-openai

import os
from getpass import getpass

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# Set your API key
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass(
        "Enter your OpenAI API key: "
    )


# Tool 1: Calculator
@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    allowed = set("0123456789+-*/(). ")

    if not all(char in allowed for char in expression):
        return "Invalid expression."

    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except (SyntaxError, ZeroDivisionError):
        return "Could not calculate the expression."


# Tool 2: Word counter
@tool
def word_counter(text: str) -> str:
    """Count the words in a text."""
    return str(len(text.split()))


tools = [calculator, word_counter]


# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Create an agent that can reason and use tools
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the calculator for arithmetic questions "
        "and the word counter for word-count questions. "
        "Answer clearly using tool results when needed."
    )
)


# Run the agent
while True:
    question = input(
        "\nAsk a question (or type 'exit'): "
    ).strip()

    if question.lower() == "exit":
        break

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    print("\nAgent response:")
    print(result["messages"][-1].content)