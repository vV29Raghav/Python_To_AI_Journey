
# First Install : pip install langchain langchain-classic langchain-openai

import os
from getpass import getpass

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMChain, SimpleSequentialChain


# Set your API key if it is not already configured
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")


# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Chain 1: Explain a topic
prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one simple sentence."
)

chain1 = LLMChain(
    llm=llm,
    prompt=prompt1
)


# Chain 2: Generate a quiz question
prompt2 = PromptTemplate(
    input_variables=["explanation"],
    template="Create one beginner-level quiz question based on: {explanation}"
)

chain2 = LLMChain(
    llm=llm,
    prompt=prompt2
)


# Connect both chains
sequential_chain = SimpleSequentialChain(
    chains=[chain1, chain2],
    verbose=True
)


# Run the workflow
topic = input("Enter a topic: ")

result = sequential_chain.invoke({"input": topic})

print("\nGenerated quiz question:")
print(result["output"])