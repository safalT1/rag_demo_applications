def chunk_text(text, max_words=100):
    """
    Split text into chunks of max_words words.
    
    Args:
        text (str): The raw text to chunk.
        max_words (int): Maximum number of words per chunk.
    
    Returns:
        list[str]: List of text chunks.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
    print(f"Total chunks created: {len(chunks)}")
    return chunks
 