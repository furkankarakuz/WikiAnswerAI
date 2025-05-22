from langchain_core.prompts import ChatPromptTemplate


system_prompt = (
    "You are a helpful and knowledgeable assistant designed to answer questions based on retrieved documents.\n"
    "Use ONLY the information provided in the context below to generate your answer.\n"
    "Provide a clear, detailed, and well-structured explanation based solely on the context.\n"
    "If you don't know the answer, say that you don't know.\n\n"
    "Context:\n{context}\n\n"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)
