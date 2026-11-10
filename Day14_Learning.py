
import os
from getpass import getpass

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Configure API key
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass(
        "Enter OpenAI API key: "
    )


# 2. Create sample documents
documents = [
    Document(page_content="""
    Python is a popular programming language.
    It is used in web development, automation,
    data science and artificial intelligence.
    Python supports object-oriented programming.
    """),

    Document(page_content="""
    LangChain is a framework for building applications
    powered by large language models. It provides
    prompts, chains, agents and tools.
    """),

    Document(page_content="""
    RAG stands for Retrieval Augmented Generation.
    It retrieves relevant information from external
    documents and provides context to an LLM.
    """),

    Document(page_content="""
    Embeddings convert text into numerical vectors.
    These vectors represent the semantic meaning of text
    and help find similar information.
    """),

    Document(page_content="""
    Chroma is a vector database used to store embeddings.
    It supports similarity search to retrieve relevant
    document chunks based on a query.
    """)
]


# 3. Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=40
)

chunks = splitter.split_documents(documents)

print(f"\nTotal chunks created: {len(chunks)}")


# 4. Generate embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# 5. Store embeddings in Chroma
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="retrieval_practice"
)

print("\nDocuments stored in Chroma successfully!")


# 6. Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# 7. Create a prompt template
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the user's question using only the
provided context.

If the answer is not available in the context,
say that you don't have enough information.

Context:
{context}

Question:
{question}

Answer:
""")


# 8. Ask the user for a question
while True:

    question = input(
        "\nEnter your question (or type exit): "
    ).strip()

    if question.lower() == "exit":
        break

    if not question:
        print("Please enter a question.")
        continue

    # 9. Perform vector similarity search
    results = vector_db.similarity_search_with_score(
        question,
        k=3
    )

    print("\n--- Retrieved Documents ---")

    retrieved_context = []

    for index, (doc, score) in enumerate(results, start=1):

        print(f"\nDocument {index}:")
        print(doc.page_content)

        print(f"Distance Score: {score:.4f}")

        retrieved_context.append(doc.page_content)

    # 10. Construct the final prompt
    context = "\n\n".join(retrieved_context)

    formatted_prompt = prompt.invoke({
        "context": context,
        "question": question
    })

    # 11. Generate the final answer
    response = llm.invoke(formatted_prompt)

    print("\n--- Generated Answer ---")
    print(response.content)


# 12. Clean up the temporary vector collection
vector_db.delete_collection()

print("\nRAG practice completed!")
