import logging
logger = logging.getLogger(__name__)
logger.debug("🐣 Entered model_router.py")

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama

def log_debug_message(message):
    logger.debug(f"🔁 {message}")

def get_model(task: str):
    if task == "qa":
        return ChatOllama(model="granite3.3:2b")
    elif task == "classifier":
        return ChatOllama(model="granite3.3:2b")
    elif task == "summarizer":
        return ChatOllama(model="granite3.3:8b")
    elif task == "chat":
        return ChatOllama(model="granite3.3:8b")
    else:
        raise ValueError(f"Unknown task: {task}")

def get_classifier_model():
    logger.debug("📊 Loading classifier model")
    return ChatOllama(model="granite3.3:2b")

def get_embeddings_model():
    logger.debug("🧠 OllamaEmbeddings initialized")
    return OllamaEmbeddings(model="nomic-embed-text")
