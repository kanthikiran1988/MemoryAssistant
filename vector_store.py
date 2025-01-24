from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from datetime import datetime

class MemoryStore:
    def __init__(self, persist_directory='./memory_db'):
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )
    
    def store_memory(self, topic: str, information: str) -> str:
        try:
            # Store the full context as a single document
            text = f"{topic}: {information}"
            self.vector_store.add_texts(
                texts=[text],
                metadatas=[{"timestamp": datetime.now().isoformat()}]
            )
            return f"I've stored that information about {topic}"
        except Exception as e:
            return f"Error storing memory: {str(e)}"
    
    def retrieve_memory(self, topic: str) -> str:
        try:
            # Perform similarity search
            results = self.vector_store.similarity_search(topic, k=3)
            if results:
                memories = []
                for doc in results:
                    memories.append(f"{doc.metadata['timestamp']}: {doc.page_content}")
                return "\n".join(memories)
            return f"I don't have any information stored about {topic}"
        except Exception as e:
            return f"Error retrieving memory: {str(e)}" 