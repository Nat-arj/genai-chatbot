from rag.embeddings import get_embeddings
from rag.retriever import get_retriever
from rag.llm import get_llm
from prompts.prompt import get_prompt


def ask_question(question):

    embeddings = get_embeddings()

    retriever = get_retriever(embeddings)

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = get_prompt()

    formatted_prompt = prompt.format(context=context,question=question)

    llm = get_llm()

    response = llm.invoke(formatted_prompt)

    return response.content