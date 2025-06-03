# LangChain OLGA — Developer Guide

This project powers *OLGA* (**Ontology-Linked Generalized Assistant**), a modular LangChain-based assistant with dynamic memory, RAG-based responses, and structured chat control. It uses LangGraph for state-driven interaction and a custom routing mechanism for persona mode switching.

---

## 🗂️ Project Structure (Updated)

```
LangChain_Olga/
├── app.py                  # CLI and control loop entry point
├── rag.py                  # RAG + memory query logic
├── chat.py                 # Local persona memory response logic
├── routing_classifier.py   # Classifies input into (mode, tool)
├── langgraph_router.py     # FSM state graph powered by LangGraph
├── tools/
│   └── responding.py       # Tool definitions for LangGraph (chat, web, qa)
├── faiss_indexes/           # FAISS vector stores for each mode
├── persona_memory/                 # Persona memory files (work.jsonl, play.jsonl, etc.)
├── prompts/                # Prompt templates for QA and chat
├── utils/                  # Model router, ingest, and classifier utils
└── run.sh                  # Wrapper for launching with debug or bench
```

---

## ⚙️ Key Files & Functions

### `app.py`
- Entrypoint, parses CLI args and launches `rag` or `run_graph()`.
- CLI flags:
  - `--debug`: enables verbose logging
  - `--bench`: runs benchmark mode instead of interactive

### `rag.py`
- `query_memory(query, mode)`: Uses FAISS vector search
- `embed_personas()`: Embeds persona memory into `faiss_indexes/`
- `query_persona_store(query, mode)`: Wraps memory query and prompt handling
- Uses `nomic-embed-text` for fast embeddings.

### `chat.py`
- `respond_with_chat_memory(prompt, mode)`: Generates contextual memory-aware chat response.

### `routing_classifier.py`
- `classify_mode_and_tool(prompt)`: Routes input into:
  - Mode: `"work"` or `"play"`
  - Tool: `"chat"`, `"web"`, `"rag"` — JSON5-encoded output
- Falls back on defaults for unparseable results.

### `langgraph_router.py`
- FSM graph defined with `OlgaState` TypedDict:
  ```python
  class OlgaState(TypedDict):
      prompt: str
      mode: str
      honorific: str
      result: str
  ```
- Uses `RunnableLambda` and `json5` for relaxed JSON validation.
- Entry and exit are both the `respond` node wrapping `search_or_respond_tool`.

### `tools/responding.py`
- Defines LangChain-compatible tools:
  - `search_or_respond_tool`: Routes based on intent and mode
  - `chat_response_tool`: Responds with memory
  - `qa_tool`: Executes structured RAG-style QA
  - `web_tool`: Uses summarizer for external web content

---

## 🧠 Memory & Persona Modes

- Stored in `persona_memory/` as `.jsonl` (e.g. `work.jsonl`, `play.jsonl`)
- Two persona modes:
  - **Work**: Technical, structured, professional
  - **Play**: Expressive, casual, emotional
- "Shared" memory for long-term factual recall
- Each mode has its own FAISS vector index in `faiss_indexes/` (e.g. `faiss_indexes/work/`)

---

## 🌐 Intent Classification and Routing

- Calls a local utility LLM with a structured prompt.
- Expects output in JSON5:
  ```json5
  {
    "mode": "work",
    "tool": "chat"
  }
  ```
- Handles invalid responses gracefully with fallback to `"work"` and `"chat"`.

---

## 🧪 Benchmarking (WIP)

- `--bench` mode runs structured test cases from a batch file (markdown or JSON)
- Logs stored in `logs/benchmark_results/`
- Chat transcripts stored in `logs/chat_sessions/`
- Emoji logging indicators: ✅ success, ❌ failure

---

## 🔍 Debug Mode

- `--debug` shows routing, model selection, prompt payloads, and tool responses.
- Memory embedding is rebuilt on file change.
- Logger outputs are color-coded for clarity.

---

## 🪄 Honorific Control

- `honorific` (e.g., `"sir"`, `"friend"`, `"user"`) is passed optionally
- Used in prompt templates but not required for logic to function

---

## 🧹 Notes

- All models run locally (Ollama integration)
- Routing is done via `model_router.py`
- No external API calls are required unless configured in `web_tool`

