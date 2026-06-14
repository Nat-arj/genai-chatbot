from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from rag.llm import get_llm
from prompts.prompt import get_prompt

pdf_path = "data/Python_Crash_Course.pdf"

documents = load_pdf(pdf_path)

chunks = split_documents(documents)
chunks = chunks[:300]

print(f"Pages Loaded: {len(documents)}")
print(f"Total Chunks: {len(chunks)}")

embeddings = get_embeddings()

print("Embedding model loaded...")

vectorstore = create_vectorstore(chunks,embeddings)

print("ChromaDB created successfully!")

