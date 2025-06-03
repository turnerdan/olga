import json5
import logging
from utils.model_router import get_classifier_model  # Updated to match task-specific naming

logger = logging.getLogger(__name__)

def classify_mode_and_tool(prompt: str) -> dict:
    """Classify input into {mode, tool} using the classifier model."""
    classifier = get_classifier_model()
    system_prompt = """You are a classifier that routes user input to a mode and tool.

Modes:
- "work": task-oriented, professional, analytical
- "play": expressive, emotional, casual

Tools:
- "chat": default conversation and memory responses
- "rag": question-answering from documents
- "web": queries involving external information or search

Respond ONLY with a JSON5 object like:
{ mode: "play", tool: "chat" }

Do not explain.
"""

    full_prompt = f"{system_prompt}\n\nUser input:\n{prompt}"
    result = classifier.invoke(full_prompt)

    try:
        return json5.loads(result.content)
    except Exception as e:
        logger.warning(f"Classifier failed to produce valid JSON5. Response:\n{result.content}")
        return {"mode": "work", "tool": "chat"}  # safe default
