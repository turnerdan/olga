from langchain.tools import tool
import logging
from chat import respond_with_chat_memory
from rag import query_persona_store
from routing_classifier import classify_mode_and_tool
from tools.web import search_web

@tool
def chat_response_tool(prompt: str, mode: str = "work") -> str:
    """Generate a response using assistant memory and persona."""
    logging.debug(f"[💬] chat_response_tool called with: prompt='{prompt}', mode='{mode}'")
    result = respond_with_chat_memory(prompt, mode=mode)
    logging.debug(f"[💬] chat_response_tool returning: {result}")
    return result

@tool
def rag_query_tool(prompt: str, mode: str = "work") -> str:
    """Retrieve an answer from embedded memory (RAG)."""
    logging.debug(f"[📚] rag_query_tool called with: prompt='{prompt}', mode='{mode}'")
    result = query_persona_store(prompt, mode=mode)
    logging.debug(f"[📚] rag_query_tool returning: {result}")
    return result

@tool
def web_search_tool(prompt: str) -> str:
    """Search the internet and return summarized results."""
    logging.debug(f"[🌐] web_search_tool called with: prompt='{prompt}'")
    result = search_web(prompt)
    logging.debug(f"[🌐] web_search_tool returning: {result}")
    return result

@tool
def search_or_respond_tool(prompt: str, mode: str = "work") -> dict:
    """Route input through RAG, web, or chat depending on classification."""
    logging.debug(f"[🧭] search_or_respond_tool routing: '{prompt}'")
    route = classify_mode_and_tool(prompt)
    tool_name = route.get("tool", "chat")
    logging.debug(f"[🧮] Routing decision: {tool_name}")

    if tool_name == "rag":
        return {"result": rag_query_tool.invoke({"prompt": prompt, "mode": mode})}
    elif tool_name == "web":
        return {"result": web_search_tool.invoke({"prompt": prompt})}
    else:
        return {"result": chat_response_tool.invoke({"prompt": prompt, "mode": mode})}
