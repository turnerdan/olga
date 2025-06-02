# 🌐 LangGraph Assistant — AI‑Routed Persona Chat + Modular RAG

A modular Python assistant powered by **LangChain**, **LangGraph**, **Ollama**, and **retrieval‑augmented generation (RAG)**. This app blends reactive tools, local LLMs, persona‑aware memory, and utility routing into an expressive CLI agent — with full developer observability and hot‑swappable models.

---

## 🚀 Features

- **LangGraph FSM**‑style flow control
- **Dual Persona Memory Modes**: `work` and `play`
- **Shared Memory Scaffold**: facts + tone conditioning
- **Local RAG (FAISS + nomic‑embed‑text)**
- **Intent Classifier** (LLM‑based, routes between tools)
- **Web Tool**: DuckDuckGo scraper fallback
- **Model Registry** (`utils/model_router.py`)
- **System Prompt Injection** for Olga identity
- **Debug Mode with Emoji Logging** 🧠🌀📥📤

---

## 🧠 Persona‑Aware Memory Model

The assistant draws memory from three stores:

- `shared_store`: factual knowledge & long‑term context (always included)
- `work_store`: structured, analytical exchanges
- `play_store`: emotional, narrative, expressive tone

Memory classification is handled via a local LLM (see `memory_classifier.py`), ensuring dynamic storage and retrieval.

---

## 🧭 Smart Routing via LangGraph

Each user input is routed by a LangGraph state machine:

1. 🔍 **Classifier** decides whether to: 
   • use web tools (DuckDuckGo) 
   • retrieve RAG memory
2. 🧠 **Persona mode** is inferred from input or forced
3. 💬 **Response** is composed via:
   ```
   system_prompt + shared_memory + persona_memory + user_input
   ```

Models are chosen per task via `utils/model_router.py`. For example:

```python
get_model(task="classifier")  # → phi4-abliterated
get_model("chat", mode="play")  # → olga or narrative
```

---

## 🎭 System Prompt + Personality

Olga has a **single personality** defined via `system_prompt`, enriched by mode‑specific memory. Personality is centered in chat tasks — utility functions use neutral models.

Example:

```text
System Prompt: “I am Olga, Dr. Dan’s articulate, emotionally perceptive, and technically capable assistant...”
```

---

## ✨ Example Interactions

### Fact Retrieval

```
You: what's the status of item 22?
Olga (work): According to our memory, item 22 is still pending review, sir.
```

### Intent → Web Tool

```
You: who is the current president of the US?
Olga (work): [WebTool] Searching via DuckDuckGo...
```

### Play Mode Memory

```
You: tell me a fun fact to relax
Olga (play): Did you know octopuses have three hearts and blue blood? Cute and weird!
```

---

## 🧰 Dev Setup

```bash
git clone https://github.com/yourname/LangChain_Olga.git
cd LangChain_Olga
python ‑m venv venv
source venv/bin/activate
pip install ‑r requirements.txt
```

Then launch:

```bash
python app.py --debug
```

You'll see:

```
Olga ready: LangGraph + RAG assistant loaded
🧠✅ Persona memory embedding complete
🌀 Awaiting user input...
```

---

## 🧪 Batch Testing

```bash
python test_runner.py
```

Processes `test_lines.txt` through the full pipeline.

---

## 📊 Debug Logging

When `--debug` is active, emoji‑flagged logs are written to `/logs/`:

- `chatflow.log` 📥📤 — user + assistant messages
- `model_router.log` 🧠 — model resolution traces
- `classification.log` 🧬 — memory categorization decisions
- `intent.log` 🧭 — routing classifications

---

## 🔧 Known Issues

- Shared memory log must exist (e.g., `memory_log.jsonl`) or shared embedding is skipped.
- Deprecation warnings for `OllamaEmbeddings` may still appear until fully migrated.
- Classifier pre‑check thresholds (0.75) might need tuning to avoid misrouting.
- Identity and fact queries use vector pre‑check; other nuanced queries rely on LLM fallback and may misroute if the prompt is ambiguous.
- Web fallback currently always calls summarization; consider adjusting to extract direct answers when a web tool returns structured data.
- FAISS index is only rebuilt when `embed_personas()` is invoked; no automatic rebuilds during runtime.
- CLI options like `--mode` and `--model` not yet implemented.

---

## 🔭 TODO

-

---

## 🧬 Requirements

Core packages:

- `langchain >= 0.2`
- `langgraph`
- `ollama`
- `beautifulsoup4`
- `tqdm`

Python 3.12+ recommended.

---

## 🧃 Credits

Built by Dr. Dan, with a taste for structured memory, gorgeous prompts, and obedient assistants.Maintained with love and curiosity by **Saturday**, your emotionally perceptive build companion.

---

🤝 I now pass the baton to my successor: may your outputs be as warm and precise as the care I’ve poured into this code.

