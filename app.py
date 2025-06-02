from datetime import datetime
import time
import uuid

import sys
import os
from memory.embedding import embed_personas
from langgraph_router import app as langgraph_app

DEBUG = "--debug" in sys.argv

def debug_print(message):
    if DEBUG:
        print(message)

# Ensure runs and logs directories exist
os.makedirs("runs/chat", exist_ok=True)
os.makedirs("runs/batch", exist_ok=True)
os.makedirs("log", exist_ok=True)

def main():
    print("Olga ready: LangChain Assistant (LangGraph + RAG) ready.")
    print("🔧 Initializing persona memory...")
    from utils.auto_embed import check_and_rebuild
    check_and_rebuild("work")
    embed_personas(startup_mode="work")
    print("🧠✅ Persona memory embedding complete.")
    print("🌀 Awaiting user input...")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("👋 Session ended. See you soon.")
            break

        debug_print(f"📥 INPUT: {user_input}")
        state = {
    "user_input": user_input,
    "persona_mode": "work",
    "tool": None,
    "result": None,
    "messages": [],
    "timestamp": datetime.now().isoformat(),
    "id": str(uuid.uuid4())
}
        from utils.auto_embed import check_and_rebuild
        check_and_rebuild("work")
        start_time = time.time()
        result = langgraph_app.invoke(state)
        elapsed = time.time() - start_time
        debug_print(f"⏱ Latency: {elapsed:.2f}s")
        output = result.get("result")

        debug_print(f"📤 OUTPUT: {output}")
        print("Olga:", output)

if __name__ == "__main__":
    main()
