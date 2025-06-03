# OLGA: Ontology-Linked Generalized Assistant

**OLGA** is a modular, local-first AI agent framework combining LangGraph state routing with Retrieval-Augmented Generation (RAG) and semantic memory. Designed for professionals, analysts, and builders, OLGA supports offline operation, persona-aware responses, and extensible task orchestration — all from your terminal.

---

## 🧠 Intelligent Local Agents, Zero Cloud Dependency

OLGA orchestrates intelligent, persona-aware logic using structured flows:

- 🧾 **Embedded Memory Recall** — vectorized markdown memory for grounded responses  
- 🕸 **Web Fallback** — live web scraping + summarization (via DuckDuckGo)  
- 🧭 **Dynamic Routing** — classifies user input and selects the best tool  
- 🪶 **Mode-Aware Output** — output adapts to `work`, `play`, or `shared` memory state  
- 🔒 **Privacy-First** — 100% offline-capable, no cloud calls required  

---

## 📁 Current Directory Layout

```
LangChain_Olga/
├── app.py                  # CLI runner and LangGraph execution
├── chat.py                 # Chat memory handler
├── rag.py                  # RAG functions and FAISS logic
├── langgraph_router.py     # LangGraph state logic and graph compilation
├── routing_classifier.py   # Query router (chat vs rag vs web)
├── ui_formatter.py         # Output formatting and CLI presentation
│
├── tools/
│   ├── responding.py       # Tool wrappers for chat, rag, web
│   └── web.py              # DuckDuckGo HTML search tool
│
├── utils/
│   └── model_router.py     # Model routing + embedding model loader
│
├── personalities/
│   ├── work.md             # Embedded persona memory (work mode)
│   ├── play.md             # Embedded persona memory (play mode)
│   └── shared/             # (planned) universal facts & context
│
├── faiss_indexes/
│   └── work/index.faiss    # FAISS index for memory embeddings
│
└── README.md               # You are here
```

---

## ⚙️ Core Functions

| Function | Description |
|----------|-------------|
| `run_graph()` | Compiles the LangGraph state machine for response execution |
| `search_or_respond_tool()` | Routes input through memory, retrieval, or search |
| `query_persona_store()` | Vector search via FAISS for semantic memory |
| `respond_with_chat_memory()` | Basic conversational fallback (mode-specific) |
| `format_response()` / `pretty_print()` | Output decoration & CLI beautification |
| `setup_logging()` | Logging toggle (quiet by default, verbose with `--debug`) |
| `validate_environment()` | Ensures FAISS index + embedding model are present |

---

## 🚀 Usage

```bash
./run.sh              # Launch OLGA in quiet mode with styled output
./run.sh --debug      # Enable verbose logging and CLI tracebacks
./run.sh --bench 5    # Run 5 benchmark prompts using RAG pipeline
```

---

## 🧪 In Development (Planned Features)

### 1. `vectorize_and_embed_documents()`
- Ingests `.docx`, `.pdf`, `.md`
- Converts to vector format for private AI memory querying
- Will support assisted summarization + live Q&A

### 2. `pretty_notify()`
- Live system feedback (terminal banners, desktop alerts, optional voice)
- Use cases: job completions, scheduled events, document ingestion status

### 3. `analyze_and_visualize_data()`
- Visual summaries from raw data (CSV, JSON, transcripts)
- CLI plots + Markdown reports
- Useful for: KPI reporting, assistant diagnostics, memory visualizations

---

## 🔖 Version

**0.6-pre** — Routing, memory, and LangGraph functional. Assistant extensions underway.
