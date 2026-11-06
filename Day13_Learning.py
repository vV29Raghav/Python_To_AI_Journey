
import os
from getpass import getpass

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA


#Configure API key
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass("Enter OpenAI API key: ")


#Create sample documents
documents = [
    Document(page_content="""
    Python is a high-level programming language.
    It is used in web development, automation,
    data science, artificial intelligence and machine learning.
    """),

    Document(page_content="""
    LangChain is a framework for building applications
    powered by large language models. It provides prompts,
    chains, agents and tools.
    """),

    Document(page_content="""
    RAG stands for Retrieval Augmented Generation.
    It retrieves relevant information from external documents
    and provides that information to an LLM to generate answers.
    """),

    Document(page_content="""
    Embeddings convert text into numerical vectors.
    Similar meanings are represented by vectors that are
    closer together in the embedding space.
    """),

    Document(page_content="""
    Chroma is a vector database used to store embeddings
    and retrieve relevant information through similarity search.
    """)
]


#Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Total chunks created:", len(chunks))


#Generate embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


#Store vectors in Chroma
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="rag_practice"
)

print("Documents stored in Chroma!")


#Create retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


#Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


#Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)


#Ask questions
while True:

    question = input("\nAsk a question (type exit to stop): ")

    if question.lower() == "exit":
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    result = qa_chain.invoke({"query": question})

    print("\nAnswer:")
    print(result["result"])

    print("\nRetrieved Context:")

    for doc in result["source_documents"]:
        print("-", doc.page_content.strip())


# Close Chroma client
vector_db.delete_collection()

