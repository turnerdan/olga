import os
import shutil

renames = {
    "memory": "persona_memory",
    "vectorstores": "faiss_indexes",
    "runs/chat": "logs/chat_sessions",
    "runs/batch": "logs/benchmark_results",
}

for old, new in renames.items():
    if os.path.exists(old):
        print(f"Moving {old} → {new}")
        parent = os.path.dirname(new)
        if parent:
            os.makedirs(parent, exist_ok=True)
        shutil.move(old, new)
    else:
        print(f"❌ Skipped missing directory: {old}")
