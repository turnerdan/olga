from langchain_ollama import ChatOllama

MODEL_REGISTRY = {
    "chat": {
        "work": "granite3.3:8b",
        "play": "huihui_ai/phi4-abliterated:latest"
    },
    "classifier": {
        "default": "granite3.3:2b"
    },
    "summarize": {
        "default": "granite3.3:2b"
    }
}

def get_model(task_type: str, mode: str = "default"):
    model_name = MODEL_REGISTRY.get(task_type, {}).get(mode, None)
    if not model_name:
        raise ValueError(f"No model found for task: {task_type}, mode: {mode}")
    print(f"🧠 Using model: {model_name} for task: {task_type}, mode: {mode}")
    return ChatOllama(model=model_name)