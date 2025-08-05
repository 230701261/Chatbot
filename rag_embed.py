from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
import uuid

client = QdrantClient(":memory:")  # Use ':memory:' for in-memory or set up local server
client.recreate_collection("news_chunks", vectors_config=VectorParams(size=384, distance=Distance.COSINE))

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=200):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def store_chunks(articles):
    for article in articles:
        chunks = chunk_text(article["text"])
        vectors = model.encode(chunks)
        payload = [{"chunk": c, "url": article["url"], "title": article["title"]} for c in chunks]
        points = [PointStruct(id=str(uuid.uuid4()), vector=v, payload=p) for v, p in zip(vectors, payload)]
        client.upsert(collection_name="news_chunks", points=points)
