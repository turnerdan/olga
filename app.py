import logging
from pathlib import Path
from datetime import datetime
import sys
import argparse

from utils.model_router import get_embeddings_model

def setup_logging(debug=False):
    log_dir = Path("logs/app")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"session_{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}.log"

    handlers = [logging.FileHandler(log_path, mode="w")]
    if debug:
        handlers.append(logging.StreamHandler(sys.stdout))

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="[{asctime}] {levelname}: {message}",
        style="{",
        handlers=handlers
    )

    logging.info("🔧 Logging initialized (debug=%s)", debug)
    logging.debug("🌀 Entered Olga CLI control flow")

def validate_environment():
    logging.debug("✅ Environment validation completed")
    store_path = Path("faiss_indexes/work/index.faiss")
    if not store_path.exists():
        logging.error("🛑 FAISS index not found at %s", store_path)
        sys.exit(1)
    try:
        _ = get_embeddings_model()
    except Exception as e:
        logging.error("🛑 Failed to load embedding model: %s", str(e))
        sys.exit(1)

def main():
    logging.debug("🚀 Inside main() execution body")
    logging.info("🚀 Starting Olga main loop...")

    from langgraph_router import run_graph
    app = run_graph()

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() in {"exit", "quit"}:
            print("Olga: 👋 Goodbye, sir.")
            break

        state = {
            "prompt": user_input,
            "mode": "work"
        }
        logging.debug(f"[🔁] Invoking LangGraph with: {state}")
        result = app.invoke(state)

        if isinstance(result, dict) and "result" in result:
            print(f"Olga: {result['result']}")
        else:
            print(f"Olga: {result}")

if __name__ == "__main__":
    print("🧭 Starting __main__ block in app.py")

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable verbose console output.")
    parser.add_argument("--bench", type=int, help="Run N benchmark prompts, e.g., --bench 5")
    args = parser.parse_args()

    print(f"⚙️ Parsed args: debug={args.debug}, bench={args.bench}")

    setup_logging(debug=args.debug)
    validate_environment()

    if args.bench:
        from rag import run_bench_subset
        run_bench_subset(args.bench)
    else:
        main()
