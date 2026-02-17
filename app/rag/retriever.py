class Retriever:
    def __init__(self, store):
        self.store = store

    def retrieve(self, query: str) -> str:
        docs = self.store.search(query)
        return "\n".join(d.page_content for d in docs)