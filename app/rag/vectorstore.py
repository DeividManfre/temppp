from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self):
        self.db = Chroma(
            persist_directory="data/chroma",
            embedding_function=OpenAIEmbeddings()
        )

    def search(self, query: str, k=4):
        return self.db.similarity_search(query, k=k)