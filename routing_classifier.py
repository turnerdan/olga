from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from utils.model_router import get_model

# Choose your utility LLM for classification
utility_llm = get_model("classifier")

def classify_mode_and_tool(text: str) -> tuple[str, str]:
    # Pre-check for identity queries to force memory
    lowered = text.strip().lower()
    if any(kw in lowered for kw in ["what is your name", "who are you", "what’s your name", "your name is", "name"]):
        return "work", "memory"
    
    """
    Use an LLM to classify user input into a persona mode and an appropriate tool.
    Returns: (mode, tool)
    """
    prompt = f"""
You are a routing classifier for an AI assistant with multiple response modes and tools.

Classify the following user input into:
- If the user asks the assistant about its own identity (e.g., "what is your name"), set tool to 'memory'

- a "persona mode": either 'work' or 'play'
- a "tool": either 'web' or 'memory'
...
Output:"""

    result = utility_llm.invoke(prompt)
    raw = result.content.strip().lower()

    # Fallback in case of malformed output
    try:
        mode, tool = [x.strip() for x in raw.split(",")]
        assert mode in {"work", "play"}
        assert tool in {"web", "memory"}
    except Exception:
        mode, tool = "work", "web"  # safe default fallback

    return mode, tool
