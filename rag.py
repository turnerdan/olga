from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from utils.logger import log_to_file
from utils.model_router import get_model
import pickle

from langchain import PromptTemplate, LLMChain
from langchain_ollama import ChatOllama
import os

# Load QA prompt template
with open(os.path.join(os.path.dirname(__file__), "qa_prompt.txt"), "r") as f:
    qa_template_str = f.read()

qa_prompt = PromptTemplate(
    input_variables=["question", "documents", "mode", "honorific"],
    template=qa_template_str
)
qa_llm = ChatOllama(model="granite3.3:8b")
qa_chain = LLMChain(llm=qa_llm, prompt=qa_prompt)

def query_persona_store(query: str, mode: str = "work", honorific: str = "") -> str:
    store_path = f"vectorstores/{mode}_store"
    with open(f"{store_path}/index.pkl", "rb") as f:
        index = pickle.load(f)
    vectorstore = FAISS.load_local(store_path, OllamaEmbeddings(model="nomic-embed-text"), index_name="index", allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)
    joined = "\n".join(doc.page_content for doc in docs)
    log_to_file("rag.log", f"[QUERY] {query}\n[RESULTS]\n{joined}")
    # Use QA chain to generate a summary/answer
    answer = qa_chain.run({
        "question": query,
        "documents": joined,
        "mode": mode,
        "honorific": honorific
    }).strip()
    return answer

def summarize_web_results(text: str, mode: str = "work", honorific: str = "") -> str:
    # Use QA chain to summarize web results
    answer = qa_chain.run({
        "question": "",
        "documents": text,
        "mode": mode,
        "honorific": honorific
    }).strip()
    log_to_file("web.log", f"[QA OUTPUT] {answer}")
    return answer

from tools.web import search_web as query_web
