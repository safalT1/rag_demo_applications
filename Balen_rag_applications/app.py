import streamlit as st
from utils.chunking import chunk_text
from utils.embedding import build_faiss_index, save_index
from utils.retrieval import retrieve_top_k
from utils.prompt import build_prompt
from utils.completion import generate_completion
from config import TEXT_FILE_PATH, FAISS_INDEX_PATH, CHUNK_MAX_WORDS, TOP_K


# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Balen Shah RAG",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Balen Shah RAG chatbot")
st.caption("Ask anything about Balen Shah based on the document.")


# ── Load and index once (cached so it doesn't re-run on every question) ────────
@st.cache_resource
def load_pipeline():
    with open(TEXT_FILE_PATH, "r", encoding="utf-8") as f:
        raw_text = f.read()

    chunks = chunk_text(raw_text, max_words=CHUNK_MAX_WORDS)
    index, chunk_mapping = build_faiss_index(chunks)
    save_index(index, FAISS_INDEX_PATH)
    return index, chunk_mapping


index, chunk_mapping = load_pipeline()


# ── Chat history ───────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ── Chat input ─────────────────────────────────────────────────────────────────
query = st.chat_input("Ask a question about Balen Shah...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            top_chunks = retrieve_top_k(query, index, chunk_mapping, k=TOP_K)
            prompt     = build_prompt(top_chunks, query)
            answer     = generate_completion(prompt)
        st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})