
import os
from getpass import getpass

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langsmith import Client, traceable


# 1. Configure API keys
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass(
        "Enter OpenAI API key: "
    )

if not os.getenv("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = getpass(
        "Enter LangSmith API key: "
    )

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "LangSmith-Practice"


# 2. Initialize LangSmith client
client = Client()


# 3. Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# 4. Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer clearly and simply."),
    ("human", "{question}")
])


# 5. Create a traced application
@traceable(name="Question Answering Application")
def answer_question(inputs: dict) -> dict:

    question = inputs["question"]

    formatted_prompt = prompt.invoke({
        "question": question
    })

    response = llm.invoke(formatted_prompt)

    return {
        "answer": response.content
    }


# 6. Test the application
print("\n--- Testing Application ---")

test_question = {
    "question": "What is Retrieval Augmented Generation?"
}

result = answer_question(test_question)

print("\nGenerated Answer:")
print(result["answer"])


# 7. Create an evaluation dataset
dataset_name = "LangSmith-Practice-Dataset"

dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="Dataset for practising LLM testing and evaluation."
)

# Questions with expected answers
examples = [
    {
        "inputs": {
            "question": "What is Python?"
        },
        "reference_outputs": {
            "answer": "Python is a programming language."
        }
    },
    {
        "inputs": {
            "question": "What is RAG?"
        },
        "reference_outputs": {
            "answer": "RAG stands for Retrieval Augmented Generation."
        }
    },
    {
        "inputs": {
            "question": "What are embeddings?"
        },
        "reference_outputs": {
            "answer": "Embeddings are numerical vector representations of data."
        }
    }
]

client.create_examples(
    dataset_id=dataset.id,
    examples=examples
)

print("\nDataset created successfully!")
print("Dataset name:", dataset.name)


# 8. Define a simple evaluator
def check_answer(outputs: dict, reference_outputs: dict) -> dict:

    actual_answer = outputs["answer"].lower()
    expected_answer = reference_outputs["answer"].lower()

    # Simple keyword-based evaluation
    score = expected_answer in actual_answer

    return {
        "key": "answer_match",
        "score": score
    }


# 9. Evaluate the application
print("\n--- Running Evaluation ---")

evaluation_results = client.evaluate(
    answer_question,
    data=dataset.name,
    evaluators=[check_answer],
    experiment_prefix="basic-llm-evaluation"
)

print("\nEvaluation completed!")
print("Check your LangSmith dashboard for results.")


# 10. Interactive testing
while True:

    question = input(
        "\nAsk a question (or type exit): "
    ).strip()

    if question.lower() == "exit":
        break

    if not question:
        print("Please enter a question.")
        continue

    try:
        result = answer_question({
            "question": question
        })

        print("\nAnswer:")
        print(result["answer"])

    except Exception as error:
        print("\nApplication error:", error)
