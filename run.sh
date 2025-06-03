#!/bin/bash

echo "[🔋] Activating virtual environment..."
source venv/bin/activate

echo "[📂] Ensuring directories are in place..."
mkdir -p logs/app logs/chat logs/batch logs/debug

echo "[🧹] Rotating old session logs..."
find logs/app -type f -name "*.log" -mtime +7 -delete

echo "=== Starting LangChain_Olga session ==="

echo "[🚀] Launching app.py with flags: $@"
python app.py "$@"
