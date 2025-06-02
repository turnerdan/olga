import os
from langgraph.graph import StateGraph
from langgraph.graph.graph import END
from routing_classifier import classify_mode_and_tool
from rag import query_persona_store, query_web, summarize_web_results
from utils.model_router import get_model

DEBUG = os.environ.get("DEBUG", "false").lower() == "true"



def classify_node(state: dict) -> dict:
    query = state["user_input"]
    mode, tool = classify_mode_and_tool(query)

    if DEBUG:
        print(f"🧭 Classifier → mode: {mode}, tool: {tool}")

    state["persona_mode"] = mode
    state["tool"] = tool
    return state

def search_or_respond_node(state: dict) -> dict:
    query = state["user_input"]
    tool = state.get("tool", "memory")
    mode = state.get("persona_mode", "work")

    if tool == "web":
        result = query_web(query)
        summary = summarize_web_results(result)
        state["result"] = summary
        return state
    result = query_persona_store(query, mode=mode)
    state["result"] = result
    return state
def generate_response_node(state: dict) -> dict:
    mode = state.get("persona_mode", "work")
    chat_model = get_model("chat", mode=mode)

    prompt = f"""
{state.get("result", "")}

Respond to the user query: "{state.get('user_input', '')}"
"""
    if DEBUG:
        print(f"🧠 Using model: {chat_model.model} for task: chat, mode: {mode}")
        print(f"📥 PROMPT:\n{prompt.strip()}")

    response = chat_model.invoke(prompt).content.strip()
    if DEBUG:
        print(f"📤 OUTPUT:\n{response}")

    state["response"] = response
    return state
workflow = StateGraph(dict)
workflow.add_node("classify", classify_node)
workflow.add_node("search_or_respond", search_or_respond_node)
workflow.add_node("generate", generate_response_node)

workflow.set_entry_point("classify")
workflow.add_edge("classify", "search_or_respond")
workflow.add_edge("search_or_respond", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()