import logging
logger = logging.getLogger(__name__)
logger.debug("🐣 Entered rag.py")

from langchain_community.vectorstores import FAISS
from langchain_core.runnables import Runnable
from langchain_core.prompts import PromptTemplate
import memory
from utils.model_router import get_model, get_embeddings_model

logger.debug("📜 Loading QA prompt...")
qa_prompt = PromptTemplate.from_template("""
You are a helpful, precise assistant answering technical questions using both the user’s documents and prior context.

User question: {question}
Relevant memory: {memory}
Retrieved context: {context}

Answer:
""")

qa_llm = get_model("qa")
try:
    qa_chain = qa_prompt | qa_llm
    logger.debug("✅ QA chain created")
except Exception as e:
    logger.exception("🔥 Failed to build QA chain")

def query_persona_store(query: str, mode: str):
    logger.debug('[🛠] Entered query_persona_store')
    store_path = f"faiss_indexes/{mode}"
    embeddings = get_embeddings_model()
    vectorstore = FAISS.load_local(store_path, embeddings, index_name="index", allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=4)
    retrieved = "\n\n".join([doc.page_content for doc in docs])

    memory_fragments = memory.get_fragments(mode)
    memory_text = "\n".join([frag["content"] for frag in memory_fragments])

    answer = qa_chain.invoke({
        "question": query,
        "context": retrieved,
        "memory": memory_text,
    })
    return answer
