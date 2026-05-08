def build_prompt(context_chunks, query):
    """
    Build a RAG prompt by combining retrieved context chunks with the user query.

    Args:
        context_chunks (list[str]): Retrieved relevant text chunks.
        query (str): The user's question.

    Returns:
        str: The formatted prompt string.
    """
    context = "\n".join(context_chunks)

    prompt = f"""You are a helpful assistant.

Use ONLY the following context to answer the question.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer in clear English:"""

    return prompt