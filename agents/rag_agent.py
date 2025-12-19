# RAG Agent – Retrieval Only

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
import os

class RAGAgent:
    def __init__(self, persist_dir="vectorstore"):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        if os.path.exists(persist_dir):
            self.db = Chroma(
                persist_directory=persist_dir,
                embedding_function=self.embeddings
            )
        else:
            docs = [
                Document(page_content="RAG improves factual accuracy of LLMs."),
                Document(page_content="Gemini is Google's large language model."),
                Document(page_content="LangGraph orchestrates agent workflows.")
            ]
            self.db = Chroma.from_documents(
                docs, self.embeddings, persist_directory=persist_dir
            )

    def retrieve(self, query, k=3):
        results = self.db.similarity_search(query, k=k)
        if not results:
            return [], []
        return [r.page_content for r in results], ["internal_doc"]
