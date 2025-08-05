import ollama

def generate_answer(context_chunks, query):
    import ollama
    context = "\n".join(context_chunks)
    prompt = f"""Use the following news snippets to answer the question:
    Context:
    {context}

    Question: {query}
    Answer:"""
    response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
