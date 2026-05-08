# 🎤 Balen Shah RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Streamlit that answers questions about Balen Shah based on source documents. The application uses FAISS for efficient semantic search and external APIs for embeddings and text completion.

## 🌟 Features

- **Document-based Q&A**: Ask questions about Balen Shah and get accurate answers based on source documents
- **Fast Retrieval**: Uses FAISS (Facebook AI Similarity Search) for efficient vector similarity search
- **Real-time Chat**: Interactive Streamlit interface with chat history
- **Semantic Understanding**: Leverages embedding models for semantic relevance
- **Configurable Pipeline**: Easy to customize chunking, retrieval, and completion parameters

## 📋 Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- API access for embeddings and completion services
- Environment variables configured (see [Configuration](#configuration))

## 🚀 Quick Start

### 1. Installation

Clone the repository and install dependencies:

```bash
cd rag_pipeline_demo
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r Balen_rag_applications/requirements.txt
```

### 2. Configuration

Copy the `.env.example` file to `.env` in the `Balen_rag_applications` directory:

```bash
cp .env.example .env
```

Then edit `.env` with your actual configuration:

```env
# API Configuration
RAG_API_KEY=your_api_key_here

# Embedding Service
EMBEDDING_URL=https://your-embedding-service-url
EMBEDDING_MODEL=your-embedding-model-name

# Completion Service
COMPLETION_URL=https://your-completion-service-url
COMPLETION_MODEL=your-completion-model-name

# Chunking Configuration
CHUNK_MAX_WORDS=100

# Retrieval Configuration
TOP_K=5

# File Paths
TEXT_FILE_PATH=./data/balen_story.txt
FAISS_INDEX_PATH=./faiss_store/index.faiss
```

### 3. Run the Application

```bash
cd Balen_rag_applications
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
rag_pipeline_demo/
├── README.md                          # This file
├── rag_pipe_demo.ipynb               # Jupyter notebook for exploration
├── venv/                             # Virtual environment
└── Balen_rag_applications/
    ├── app.py                        # Main Streamlit application
    ├── config.py                     # Configuration management
    ├── requirements.txt              # Python dependencies
    ├── data/
    │   └── balen_story.txt          # Source document about Balen Shah
    ├── faiss_store/
    │   └── index.faiss              # Prebuilt FAISS vector index
    └── utils/
        ├── __init__.py
        ├── chunking.py              # Text chunking logic
        ├── embedding.py             # FAISS index creation & management
        ├── retrieval.py             # Vector similarity search
        ├── prompt.py                # Prompt construction
        └── completion.py            # LLM-based text completion
```

## 🔧 How It Works

### 1. **Text Chunking** (`utils/chunking.py`)
   - Splits the source document into manageable chunks
   - Configurable max words per chunk (default: 100)

### 2. **Embedding & Indexing** (`utils/embedding.py`)
   - Converts text chunks into embeddings using external API
   - Builds FAISS index for fast similarity search
   - Saves index for reuse

### 3. **Retrieval** (`utils/retrieval.py`)
   - Embeds user query
   - Searches FAISS index for top-K similar chunks
   - Returns relevant context for answer generation

### 4. **Prompt Building** (`utils/prompt.py`)
   - Constructs prompts with retrieved context
   - Combines query with relevant document passages

### 5. **Completion** (`utils/completion.py`)
   - Calls LLM API with constructed prompt
   - Generates contextually relevant answers

## 📦 Dependencies

- **streamlit**: Web framework for the interactive UI
- **faiss-cpu**: Efficient similarity search library
- **numpy**: Numerical computing
- **requests**: HTTP client for API calls
- **python-dotenv**: Environment variable management

## 🎯 Usage Example

1. Start the application
2. Type a question: "Tell me about Balen Shah's career"
3. The chatbot will:
   - Search the document for relevant passages
   - Build a context-aware prompt
   - Generate and display an answer

## ⚙️ Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `CHUNK_MAX_WORDS` | Words per text chunk | 100 |
| `TOP_K` | Number of chunks to retrieve | 5 |
| `EMBEDDING_MODEL` | Model name for embeddings | Set in .env |
| `COMPLETION_MODEL` | Model for text generation | Set in .env |
| `TEXT_FILE_PATH` | Path to source document | `./data/balen_story.txt` |
| `FAISS_INDEX_PATH` | Path to FAISS index | `./faiss_store/index.faiss` |

**Note:** File paths are automatically resolved relative to the application directory. You can override them in `.env` if needed. Default paths work for both local and cloud deployments (Streamlit Cloud, Hugging Face Spaces, etc.).

## 🔄 Data Flow

```
User Query
    ↓
Embed Query (Embedding API)
    ↓
Search FAISS Index
    ↓
Retrieve Top-K Chunks
    ↓
Build Prompt with Context
    ↓
Send to Completion API
    ↓
Display Answer in Chat
```

## 📝 Development

### Adding New Features

1. Modify relevant utility files in `utils/`
2. Update configuration in `config.py` if needed
3. Update `app.py` to use new features
4. Test changes using the Streamlit UI

### Notebook Exploration

Use `rag_pipe_demo.ipynb` for experimentation and testing of individual components before integrating into the main app.

## 🐛 Troubleshooting

- **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **FAISS index not found**: Run the app once to generate the index
- **API errors**: Verify `.env` file has correct credentials and URLs
- **Slow retrieval**: Reduce `CHUNK_MAX_WORDS` or `TOP_K` for faster results

## 📄 License

This project is provided as-is for educational and research purposes.

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

---

**Built with ❤️ using Streamlit, FAISS, and RAG techniques**
