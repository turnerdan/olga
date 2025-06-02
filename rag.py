
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from utils.logger import log_to_file
from utils.model_router import get_model
import pickle

def query_persona_store(query: str, mode: str = "work") -> str:
    store_path = f"vectorstores/{mode}_store"
    with open(f"{store_path}/index.pkl", "rb") as f:
        index = pickle.load(f)
    vectorstore = FAISS.load_local(store_path, OllamaEmbeddings(model="nomic-embed-text"), index_name="index", allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)
    joined = "\n".join(doc.page_content for doc in docs)
    log_to_file("rag.log", f"[QUERY] {query}\n[RESULTS]\n{joined}")
    return joined

def summarize_web_results(text: str) -> str:
    summarizer = get_model(task_type="summarize")
    prompt = f"Summarize the following search result into a clear 2-3 sentence reply:\n{text}"
    log_to_file("web.log", f"[INPUT] {prompt}")
    result = summarizer.invoke(prompt).content.strip()
    log_to_file("web.log", f"[OUTPUT] {result}")
    return result


from tools.web import search_web as query_web
