from langchain_chroma import Chroma

def get_retriever(embeddings):
    
    vectorstore = Chroma(persist_directory="chroma_db",embedding_function=embeddings)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return retriever