# OLGA: Local Graph Assistant (LangGraph + RAG)

*OLGA* (**Ontology-Linked Generalized Assistant**),is a local-first AI assistant that combines LangGraph routing, embedded memory search, and flexible persona modes. It runs entirely offline with support for model customization, multimodal extensions, and live CLI interaction.

---

## 🌐 Overview

OLGA uses LangGraph to control how inputs are processed — switching dynamically between:
- **Chat memory recall**
- **Retrieval-Augmented Generation (RAG)**
- **Web search + summarization**

Modes (`work`, `play`, `shared`) allow different responses depending on the user's context.

---

## 📁 Directory Structure

```
LangChain_Olga/
├── app.py                    # Entry point, CLI runner, logging setup
├── chat.py                   # Conversational memory fallback handler
├── rag.py                    # RAG logic using vectorized markdown embeddings
├── langgraph_router.py       # Graph definition, state schema, and runner
├── routing_classifier.py     # Classifies user prompt into chat, rag, or web
├── ui_formatter.py           # CLI decoration + response formatting
│
├── /tools/
│   ├── responding.py         # Shared tool wrappers (chat, rag, web, combo)
│   └── web.py                # Simple DuckDuckGo HTML parser
│
├── /utils/
│   └── model_router.py       # Handles model loading and embedding routing
│
├── /personalities/
│   ├── work.md               # Embedded memory (work context)
│   ├── play.md               # Embedded memory (play context)
│   └── shared/               # (planned) universal facts & context
│
├── /faiss_indexes/
│   └── work/index.faiss      # Vector index for embedded memories
│
└── README.md                 # Project documentation
```

---

## ⚙️ Core Functions

| Function | Description |
|---------|-------------|
| `run_graph()` | Builds the LangGraph response pipeline from `langgraph_router.py` |
| `search_or_respond_tool()` | Routes input to memory (chat), vector search (rag), or `web_search_tool()` |
| `query_persona_store()` | Runs FAISS similarity search against embedded `.md` persona |
| `respond_with_chat_memory()` | Generates conversational response from persona files |
| `format_response()` / `pretty_print()` | Applies CLI output styling depending on mode |
| `setup_logging()` | Centralized logging system for debug vs normal modes |
| `validate_environment()` | Ensures FAISS and embedding model are present |

---

## 🚀 Usage

```bash
./run.sh              # Launch Olga in quiet mode with styled output
./run.sh --debug      # Enable verbose logging and CLI tracebacks
./run.sh --bench 5    # Run 5 benchmark prompts via RAG
```

---

## 📈 Coming Soon

### 1. `vectorize_and_embed_documents()`
- Ingests `.docx`, `.pdf`, `.md`
- Converts content into persona-aligned FAISS vectors
- Enables assistant-guided Q&A and summarization over private files

### 2. `pretty_notify()`
- Optional live system notifications
- CLI banners, desktop alerts, or speech feedback
- Used for: task updates, reminders, background job completion

### 3. `analyze_and_visualize_data()`
- Visual summaries (charts, histograms, tables)
- Inputs: raw text, CSV, JSON
- Outputs: CLI markdown or Matplotlib visuals

---

## 🔖 Version
**0.6-pre** — Routing, memory, and LangGraph functional. Extensions incoming.

