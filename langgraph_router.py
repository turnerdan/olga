import logging
logger = logging.getLogger(__name__)
logger.debug("🛰️ Logger initialized in langgraph_router")

from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

from tools.responding import search_or_respond_tool
import json5

# Define a TypedDict for state schema
class OlgaState(TypedDict):
    prompt: str
    mode: str
    result: str

# Create a lambda to wrap the tool and isolate the 'prompt' and 'mode' inputs
search_or_respond_lambda = RunnableLambda(
    lambda state: search_or_respond_tool.invoke({
        "prompt": state["prompt"],
        "mode": state["mode"]
    })
)

# Use this typed dict class directly as the schema
graph = StateGraph(OlgaState)
graph.add_node("respond", search_or_respond_lambda)
graph.set_entry_point("respond")
graph.set_finish_point("respond")

def run_graph():
    return graph.compile()
