#!/usr/bin/env python3
"""
ingest_pdf.py

Generic script to ingest PDF documents into a FAISS vectorstore.

Usage:
    python ingest_pdf.py --pdf_path /path/to/document.pdf --store_path vectorstores/work_store

Requirements:
    pip install langchain llama-cpp faiss-cpu PyPDF2

This script will:
    1. Load the specified PDF using PyPDFLoader.
    2. Split the document into ~1000-character chunks.
    3. Embed each chunk using OllamaEmbeddings (nomic-embed-text).
    4. Append to or create a FAISS index at the given store path.
"""

import os
import argparse

# ——— Updated paths to avoid deprecation warnings ———
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Make sure you have `pip install langchain-ollama` so this import works
from langchain_ollama import OllamaEmbeddings

def load_and_chunk(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = splitter.split_documents(documents)
    return chunks

def upsert_to_store(chunks, store_path: str):
    # Initialize OllamaEmbeddings (e.g., nomic-embed-text)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # If store already exists, load it and append
    if os.path.isdir(store_path) and os.path.exists(os.path.join(store_path, "index.faiss")):
        faiss_index = FAISS.load_local(
            store_path,
            embeddings,
            index_name="index",
            allow_dangerous_deserialization=True
        )
        faiss_index.add_documents(chunks)
        print(f"➕ Appended {len(chunks)} chunk(s) to existing store at '{store_path}'.")
    else:
        os.makedirs(store_path, exist_ok=True)
        faiss_index = FAISS.from_documents(
            chunks,
            embeddings,
            index_name="index"
        )
        print(f"✅ Created new store and added {len(chunks)} chunk(s) at '{store_path}'.")

    faiss_index.save_local(store_path)
    print(f"✔️ Saved FAISS index to '{store_path}'.")

def main():
    parser = argparse.ArgumentParser(description="Ingest a PDF into a FAISS store via OllamaEmbeddings.")
    parser.add_argument("--pdf_path", type=str, required=True, help="Path to the PDF document.")
    parser.add_argument("--store_path", type=str, required=True, help="Directory for FAISS store.")
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        raise FileNotFoundError(f"Could not find PDF at '{args.pdf_path}'")

    print(f"Loading and splitting PDF: {args.pdf_path} ...")
    chunks = load_and_chunk(args.pdf_path)

    print(f"Embedding and merging into store ({args.store_path}) ...")
    upsert_to_store(chunks, args.store_path)

if __name__ == "__main__":
    main()
