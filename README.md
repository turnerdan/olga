# LangGraph Assistant

A modular Python-based AI assistant framework leveraging LangChain and LangGraph for persona-driven chat and Retrieval-Augmented Generation (RAG). Designed for developers, this documentation outlines major files, functions, features, and modes.

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration and Environment](#configuration-and-environment)
- [Major Files and Functions](#major-files-and-functions)
  - [run.sh](#runsh)
  - [app.py](#apppy)
  - [langgraph_router.py](#langgraph_routerpy)
  - [routing_classifier.py](#routing_classifierpy)
  - [rag.py](#ragpy)
  - [memory.py & persona.py](#memorypy--personapy)
  - [summarize.py](#summarizepy)
  - [tools.py](#toolspy)
  - [utils/model_router.py](#utilsmodel_routerpy)
  - [utils/auto_embed.py](#utilsauto_embedpy)
- [Memory Modes and Features](#memory-modes-and-features)
- [Retrieval-Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
- [Intent Classification and Routing](#intent-classification-and-routing)
- [Web Tool Fallback](#web-tool-fallback)
- [Logging and Observability](#logging-and-observability)
- [Requirements](#requirements)
- [License](#license)

## Overview

LangGraph Assistant provides a finite-state machine (FSM) approach to flow control, enabling dual persona memory modes (`work` and `play`), shared memory scaffolding for persistent facts, and modular integration of local RAG using FAISS and embedding models. The assistant routes user inputs through an LLM-based classifier to determine whether to invoke persona-based responses, summarization, or web search tools.

## Directory Structure

```
/
├── app.py
├── run.sh
├── langgraph_router.py
├── routing_classifier.py
├── rag.py
├── memory.py
├── persona.py
├── summarize.py
├── tools.py
├── requirements.txt
├── README.md
├── utils/
│   ├── model_router.py
│   └── auto_embed.py
├── memory/
│   ├── embedding.py
│   └── __init__.py
├── vectorstores/
│   ├── work_store/
│   └── play_store/
└── vis/
    └── README.md
```

- **app.py**: Main entry point for the assistant.
- **run.sh**: Shell script to initialize environment and launch app.
- **langgraph_router.py**: Manages FSM routing logic using LangGraph.
- **routing_classifier.py**: Classifies user inputs into modes and tools.
- **rag.py**: Handles embedding-based search over persona memory.
- **memory.py & persona.py**: Utilities for memory management and persona loading.
- **summarize.py**: Summarization routines applied to external content.
- **tools.py**: Defines auxiliary tools (e.g., web scraper).
- **utils/model_router.py**: Registry and router for selecting local LLM models.
- **utils/auto_embed.py**: Automates embedding of persona memory.
- **vectorstores/**: Stores FAISS indexes for `work` and `play` memory modes.
- **vis/**: Visualization assets and README for data visualization.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Set up Python environment** (Python 3.12+ recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Verify dependencies**:
   - `langchain`
   - `nomic-embed-text`
   - `faiss` (or `faiss-cpu` / `faiss-gpu`)
   - `tqdm`
   - `duckduckgo-search`

## Usage

Execute the assistant using the provided shell script:

```bash
chmod +x run.sh
./run.sh [--debug]
```

- `--debug`: Enable verbose logging and developer observability.
- The script will:
  - Activate the virtual environment.
  - Ensure necessary directories exist.
  - Rotate old session logs.
  - Initialize and embed persona memory.
  - Launch `app.py` with specified flags.

Alternatively, run `app.py` directly:

```bash
python app.py --debug
```

## Configuration and Environment

- **Environment Variables**:
  - `OPENAI_API_KEY`: If using OpenAI endpoints for fallback.
  - `SCRAPER_API_KEY`: API key for DuckDuckGo scraper (optional).
- **Configuration Files**:
  - `env`: Shell variables loaded by `run.sh`.
- **Vectorstore Paths**:
  - Default FAISS indexes stored under `vectorstores/work_store/` and `vectorstores/play_store/`.

## Major Files and Functions

### run.sh

- **Purpose**: Automates environment activation, directory setup, log rotation, memory embedding, and application launch.
- **Key Steps**:
  1. Activate Python virtual environment.
  2. Create directories: `runs/chat/`, `runs/batch/`, `logs/`.
  3. Rotate old logs in `logs/`.
  4. Call `python -c "from memory import embed_personas; embed_personas()"`.
  5. Launch `app.py` with passed flags.
- **Usage**:
  ```bash
  ./run.sh --debug
  ```

### app.py

- **Purpose**: Main application script; initializes components, reads command-line flags, and enters interactive chat loop.
- **Key Functions**:
  - `main()`: Parses arguments, initializes memory and model routers, and starts LangGraph FSM.
  - Error handling and graceful shutdown.
- **Flags**:
  - `--debug`: Enables debug-level logging.
  - `--mode [work|play|shared]`: (Optional) Start assistant in specific persona mode.

### langgraph_router.py

- **Purpose**: Defines FSM states and transitions for chat flow; integrates with LangGraph library.
- **Key Components**:
  - `ChatState`: Data class holding user state (e.g., `persona_mode`, `chat_history`).
  - FSM definition: States like `classify`, `respond_persona`, `search_fallback`, `summarize_response`.
- **Logging Hooks**: Captures prompts, model responses, and routing decisions.

### routing_classifier.py

- **Purpose**: Classifies incoming user messages to determine persona mode (`work` or `play`) and required tool.
- **Key Function**:
  - `classify_mode_and_tool(user_input: str, state: ChatState) -> Tuple[str, Optional[str]]`: Returns mode and tool name (e.g., `None` for direct persona response, `"summarizer"`, `"web_search"`).
- **Trainable LLM-based Classifier**: Uses a local model (configured in `utils/model_router.py`) to infer intent.

### rag.py

- **Purpose**: Embeds and queries persona memory using FAISS.
- **Key Functions**:
  - `embed_personas()`: Iterates through persona files under `memory/`, generates embeddings (via `nomic-embed-text`), and stores FAISS indexes.
  - `query_persona_store(query: str, mode: str) -> str`: Retrieves relevant memory fragments based on `mode` and returns concatenated context.
- **Vectorstore Structure**:
  ```
  vectorstores/
  ├── work_store/
  └── play_store/
  ```
- **Usage**: Called during initialization or when memory changes are detected.

### memory.py & persona.py

- **memory.py**:
  - **Purpose**: Loads and manages memory fragments from `memory_log.jsonl`.
  - **Key Functions**:
    - `load_memory(mode: str) -> List[Dict]`: Loads JSONL entries for `work`, `play`, or `shared`.
    - `append_memory(fragment: str, mode: str)`: Appends new memory to log file.
- **persona.py**:
  - **Purpose**: Defines persona-specific metadata and configuration.
  - **Key Data Structures**:
    - Persona templates (e.g., system prompts, tone guidelines for `work` and `play` modes).

### summarize.py

- **Purpose**: Handles summarization of long or unstructured external responses (e.g., web search results).
- **Key Functions**:
  - `summarize_text(text: str) -> str`: Uses a local summarization model to condense input text.
  - Integration point: Invoked when `routing_classifier` directs flow to summarization.

### tools.py

- **Purpose**: Implements auxiliary tools available to the assistant.
- **Key Tools**:
  - `web_search(query: str) -> str`: Scrapes DuckDuckGo (or other search engine) and returns a summarized snippet.
  - `duckduckgo_search`: Low-level helper function using `duckduckgo-search` library.
- **Error Handling**: Falls back to open APIs if local scrapers fail.

### utils/model_router.py

- **Purpose**: Central registry for selecting and instantiating local LLMs.
- **Key Components**:
  - `get_model(name: str)`: Returns a model handle (e.g., LLM wrapper) based on configuration.
  - Default mappings (e.g., `"ayla"` → `ChatOllama(model="Ayla-Light-v2")`).
- **Usage**: Used by `routing_classifier`, `rag`, and `summarize`.

### utils/auto_embed.py

- **Purpose**: Automates embedding workflow for persona memory.
- **Key Function**:
  - `auto_embed_on_change()`: Watches memory directory for changes and triggers `embed_personas()` as needed.
- **Integration**: Can be configured to run as a background thread or via file watcher.

## Memory Modes and Features

- **Work Mode**:
  - Goal: Provide task-oriented, technical assistance.
  - Tone: Formal, concise, professional.
  - Memory: Uses `vectorstores/work_store/` to supply relevant context.

- **Play Mode**:
  - Goal: Support casual, narrative, or expressive interactions.
  - Tone: Informal, emoji-rich, conversational.
  - Memory: Uses `vectorstores/play_store/` to supply relevant context.

- **Shared Memory**:
  - Holds long-term user facts, preferences, and persistent data.
  - Shared across both `work` and `play` for continuity.

## Retrieval-Augmented Generation (RAG)

1. **Embedding Creation**:
   - Persona files under `memory/` (e.g., Markdown or JSON files) are tokenized and embedded using `nomic-embed-text`.
   - FAISS indexes built and stored in `vectorstores/`.

2. **Querying**:
   - User queries routed by `routing_classifier` to `rag.query_persona_store`.
   - Retrieves top-N similar fragments and assembles context.

3. **Response Generation**:
   - The selected context is prepended to LLM prompts for persona-consistent replies.

## Intent Classification and Routing

- **routing_classifier.py**:
  - Evaluates whether user input is a direct question (ends with `?`), a command, or an off-topic request.
  - Routes to:
    - **Persona Response**: If no special tool is needed.
    - **Summarization**: If summarizer should process unstructured data.
    - **Web Search**: If external info is required.
- **LangGraph FSM**:
  - States include: `classify`, `respond_persona`, `summarize`, `web_search`, `finalize`.
  - Transition logic defined in `langgraph_router.py`.

## Web Tool Fallback

- **tools.py**:
  - Primary: Local web scraper for DuckDuckGo via `duckduckgo-search`.
  - Secondary: Open APIs or simple HTTP requests if scraper fails.
  - Returns raw text or summarized snippet for LLM to process.

## Logging and Observability

- **Logs**:
  - Chat logs stored under `runs/chat/`.
  - Batch/benchmark logs stored under `runs/batch/`.
  - Log rotation handled in `run.sh`.
  - Debug mode (`--debug`) increases verbosity, showing:
    - Routing decisions.
    - Prompts sent to models.
    - Model responses.
- **Visual Indicators**:
  - Success: ✅
  - Failure: ❌

## Requirements

- Python 3.12+
- Install via:
  ```bash
  pip install -r requirements.txt
  ```
- Sample dependencies:
  - `langchain`
  - `nomic-embed-text`
  - `faiss-cpu` (or GPU variant)
  - `duckduckgo-search`
  - `tqdm`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
