from rag_embed import client, model

def get_relevant_chunks(query, top_k=3):
    q_vector = model.encode([query])[0]
    hits = client.search("news_chunks", query_vector=q_vector, limit=top_k)
    return [hit.payload['chunk'] for hit in hits]
