
from utils.model_router import get_model
from utils.logger import log_and_print

def summarize_text_with_llm(text: str, debug=True) -> str:
    model = get_model(task_type="summarize")
    prompt = f"Summarize the following web search results into 1–2 clear sentences:\n\n{text.strip()}"
    log_and_print("summarize_prompt", prompt, debug=debug)
    result = model.invoke(prompt)
    summary = result.content.strip()
    log_and_print("summarize_result", summary, debug=debug)
    return summary
