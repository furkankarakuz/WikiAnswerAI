from langchain_chroma import Chroma
from process.prompt_process import prompt
from langchain.chains import create_retrieval_chain
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI


def wiki_search(*args):
    return WikipediaLoader(*args).load()


class RagWiki():
    def __init__(self, documents, model_info, chunk_info):
        self.documents = documents
        self.model_info = model_info
        self.chunk_info = chunk_info

        self.embedding_models = {"Gemini": lambda: GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=model_info["api_key"]), "GPT": lambda: OpenAIEmbeddings(model="text-embedding-3-small", api_key=model_info["api_key"])}[model_info["model_type"]]
        self.chat_models = {"Gemini": lambda: ChatGoogleGenerativeAI(model=model_info["model_name"], google_api_key=model_info["api_key"]), "GPT": lambda: ChatOpenAI(model=model_info["model_name"], api_key=model_info["api_key"])}[model_info["model_type"]]

        self.calculate_similarity(documents, chunk_info["chunk_size"], chunk_info["chunk_overlap"])

    def calculate_similarity(self, documents, chunk_size, chunk_overlap):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(documents)

        vectorstore = Chroma.from_documents(docs, self.embedding_models())
        self.retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    def get_answer(self, question):
        question_answer_chain = create_stuff_documents_chain(self.chat_models(), prompt)
        rag_chain = create_retrieval_chain(self.retriever, question_answer_chain)
        response = rag_chain.invoke({"input": question})

        return {"answer": response["answer"], "source": {doc.metadata["title"]: doc.metadata["source"] for doc in response["context"]}}
