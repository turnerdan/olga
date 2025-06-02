#!/usr/bin/env bash
#
# run.sh — Robust wrapper script for cold-starting LangChain_Olga
#
# Usage:
#   chmod +x run.sh
#   ./run.sh [--debug]
#

# === Configuration ===
VENV_DIR="venv"
APP_SCRIPT="app.py"
LOG_DIR="logs"
RUN_DIR="runs/chat"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
SESSION_LOG="${LOG_DIR}/session_${TIMESTAMP}.log"

# Extra flags passed through to python (e.g., --debug)
PYTHON_FLAGS="$*"

# === Helper Function ===
echotime() {
  echo "[$(date +"%H:%M:%S")] $*"
}

# === 1. Ensure venv exists ===
if [ ! -d "${VENV_DIR}" ]; then
  echotime "⚠️  Virtual environment not found. Creating ${VENV_DIR}..."
  python3 -m venv "${VENV_DIR}"
  echotime "🛠  Installing dependencies..."
  source "${VENV_DIR}/bin/activate"
  pip install --upgrade pip
  pip install -r requirements.txt
  deactivate
fi

# === 2. Activate venv ===
echotime "🔋 Activating virtual environment..."
source "${VENV_DIR}/bin/activate"

# === 3. Prepare directories ===
echotime "📂 Ensuring directories are in place..."
mkdir -p "${LOG_DIR}"
mkdir -p "${RUN_DIR}"

# === 4. Rotate or clear old logs (keep last 10) ===
echotime "🧹 Rotating old session logs..."
# List logs sorted by time, skip first 10, delete the rest
ls -1t ${LOG_DIR}/session_*.log 2>/dev/null | tail -n +11 | xargs -r rm -f || true

# === 5. Session Banner ===
echotime "=== Starting LangChain_Olga session ===" | tee -a "${SESSION_LOG}"

# === 6. Auto-embed check (FAISS rebuild if needed) ===
echotime "🔄 Checking for memory/persona updates..."
python3 - <<'PYCODE' 2>&1 | tee -a "${SESSION_LOG}"
from utils.auto_embed import check_and_rebuild
check_and_rebuild("work")
PYCODE

# === 7. Launch the app ===
echotime "🚀 Launching app.py with flags: ${PYTHON_FLAGS}"
python3 "${APP_SCRIPT}" ${PYTHON_FLAGS} 2>&1 | tee -a "${SESSION_LOG}"

# === 8. Session End Banner ===
echotime "=== Session ended ===" | tee -a "${SESSION_LOG}"

# === 9. Deactivate venv ===
echotime "🔌 Deactivating virtual environment..."
deactivate

exit 0
