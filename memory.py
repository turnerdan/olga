# rolling_memory.py
from collections import deque
import json
import os

class RollingMemory:
    def __init__(self, max_len=99, log_path="memory_log.jsonl"):
        self.max_len = max_len
        self.memory = deque(maxlen=max_len)
        self.log_path = log_path
        self._load_log()

    def _load_log(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        self.memory.append(entry)
                    except json.JSONDecodeError:
                        continue

    def save_log(self):
        with open(self.log_path, "w", encoding="utf-8") as f:
            for entry in self.memory:
                json.dump(entry, f)
                f.write("\n")

    def append(self, user_input, assistant_response):
        self.memory.append({
            "user": user_input,
            "assistant": assistant_response
        })

    def get_context(self):
        return list(self.memory)

    def print_trace(self):
        for i, msg in enumerate(self.memory):
            print(f"[{i+1}] You: {msg['user']}")
            print(f"      Assistant: {msg['assistant']}")


memory = RollingMemory(max_len=99)


def get_fragments(mode: str):
    import os, json
    path = f"persona_memory/{mode}.jsonl"
    fragments = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    fragments.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return fragments
