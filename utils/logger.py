
import os

LOG_PATH = "log/graph.log"
os.makedirs("log", exist_ok=True)

def log_to_file(tag: str, content: str):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n[{tag.upper()}]\n{content}\n{'-'*40}\n")

def log_and_print(tag: str, content: str, debug=True):
    if debug:
        print(f"🔍 [{tag.upper()}] {content}")
    log_to_file(tag, content)
