import os
import time
from pathlib import Path
from memory.embedding import embed_personas

# Store last modified times in a simple dict
_last_mod_times = {}

def check_and_rebuild(startup_mode="work"):
    """
    Check if memory_log.jsonl or any persona file has changed since the last check.
    If so, re-run embed_personas(startup_mode).
    """
    global _last_mod_times
    sources = {
        "shared": Path("memory_log.jsonl"),
        "work": Path("personalities/work.md"),
        "play": Path("personalities/play.md")
    }

    rebuild_needed = False

    for key, path in sources.items():
        if not path.exists():
            continue
        mod_time = path.stat().st_mtime
        last_time = _last_mod_times.get(key)
        if last_time is None or mod_time > last_time:
            rebuild_needed = True
            _last_mod_times[key] = mod_time

    if rebuild_needed:
        print("🔄 Changes detected in memory or persona files. Rebuilding FAISS index...")
        embed_personas(startup_mode)
