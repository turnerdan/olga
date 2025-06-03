from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os
from pathlib import Path
import json

def embed_personas(startup_mode="work"):
    """Embeds 'shared' memory and the given persona (e.g., 'work') into FAISS vectorstores."""
    print("🔧 Embedding persona memory...")

    base_path = Path("personalities")
    store_path = Path("vectorstores")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=20)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Embed shared memory from memory_log.jsonl
    shared_log = Path("memory_log.jsonl")
    if not shared_log.exists():
        print(f"⚠️ No shared memory log found at {shared_log}; skipping shared embedding.")
    else:
        with open(shared_log, "r", encoding="utf-8") as f_log:
            content = ""
            for line in f_log:
                try:
                    obj = json.loads(line)
                    content += obj.get("user", "") + "\n" + obj.get("assistant", "") + "\n"
                except:
                    continue
            if content.strip() == "":
                print("⚠️ Shared memory log is empty; skipping shared embedding.")
            else:
                documents = [Document(page_content=chunk) for chunk in text_splitter.split_text(content)]
                vectorstore = FAISS.from_documents(documents, embeddings)
                store_dir = store_path / f"shared_store"
                vectorstore.save_local(store_dir, index_name="index")
                print(f"✅ Embedded and saved shared memory at {store_dir}/index.faiss")

    # Embed the startup_mode persona (e.g., 'work')
    mode = startup_mode
    file_path = base_path / f"{mode}.md"
    if not file_path.exists():
        print(f"⚠️ Missing personality file: {file_path}; skipping {mode} embedding.")
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = f.read()
        documents = [Document(page_content=chunk) for chunk in text_splitter.split_text(raw)]
        vectorstore = FAISS.from_documents(documents, embeddings)
        store_dir = store_path / f"{mode}_store"
        vectorstore.save_local(store_dir, index_name="index")
        print(f"✅ Embedded and saved {mode} persona memory at {store_dir}/index.faiss")
