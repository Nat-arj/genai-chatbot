from langchain_core.prompts import ChatPromptTemplate

def get_prompt():

    template = """
    You are a helpful assistant.

    Use only the provided context to answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    return ChatPromptTemplate.from_template(template)