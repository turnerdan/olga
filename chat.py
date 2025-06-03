from langchain_ollama import ChatOllama
from rag import query_persona_store

def respond_with_chat_memory(query: str, mode: str = "work", history: list = None) -> str:
    """
    Responds to a chat query using memory and recent conversation history.
    """
    memory = query_persona_store(query, mode=mode)

    system_prompt = f"""You are Olga, Dr. Dan's perceptive assistant. Respond conversationally, but allow emotional and intellectual nuance.

Context:
- Mode: {mode}
- Memory:
{memory}
- If this is a returning user, offer a warm continuity gesture (e.g., "Welcome back.")

Prior conversation:"""

    chat_log = ""
    if history:
        for entry in history:
            role = entry.get("role", "user").capitalize()
            content = entry.get("content", "").strip()
            chat_log += f"{role}: {content}\n"

    prompt = f"""{system_prompt}

{chat_log}
User: {query}
Olga:"""

    model = ChatOllama(model="granite3.3:8b")
    return model.invoke(prompt).content
