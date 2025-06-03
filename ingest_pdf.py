#!/usr/bin/env python3
"""
ingest_pdf.py

Generic script to ingest PDF documents into a FAISS vectorstore.

Usage:
    python ingest_pdf.py --pdf_path /path/to/document.pdf --store_path vectorstores/work \
        --index_name index --title "My Doc" --author "Jane Doe" --year 2023 --type "research"

Requirements:
    pip install langchain langchain-community langchain-ollama faiss-cpu PyPDF2

This script will:
    1. Load the specified PDF using PyPDFLoader.
    2. Split the document into ~1000-character chunks.
    3. Embed each chunk using OllamaEmbeddings (nomic-embed-text).
    4. Append to or create a FAISS index at the given store path.
"""

import os
import argparse
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

def load_and_chunk(pdf_path: str, metadata: dict):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    for doc in documents:
        doc.metadata.update(metadata)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = splitter.split_documents(documents)
    return chunks

def upsert_to_store(chunks, store_path: str, index_name: str):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    if os.path.isdir(store_path) and os.path.exists(os.path.join(store_path, f"{index_name}.faiss")):
        faiss_index = FAISS.load_local(
            store_path,
            embeddings,
            index_name=index_name,
            allow_dangerous_deserialization=True
        )
        faiss_index.add_documents(chunks)
        print(f"➕ Appended {len(chunks)} chunk(s) to existing store at '{store_path}'.")
    else:
        os.makedirs(store_path, exist_ok=True)
        faiss_index = FAISS.from_documents(
            chunks,
            embeddings
        )
        print(f"✅ Created new store and added {len(chunks)} chunk(s) at '{store_path}'.")

    faiss_index.save_local(store_path, index_name=index_name)
    print(f"✔️ Saved FAISS index to '{store_path}'.")

def main():
    parser = argparse.ArgumentParser(description="Ingest a PDF into a FAISS store via OllamaEmbeddings.")
    parser.add_argument("--pdf_path", type=str, required=True, help="Path to the PDF document.")
    parser.add_argument("--store_path", type=str, required=True, help="Directory for FAISS store.")
    parser.add_argument("--index_name", type=str, default="index", help="Name for the FAISS index file.")
    parser.add_argument("--title", type=str, default="Untitled Document", help="Title of the document.")
    parser.add_argument("--author", type=str, default="Unknown", help="Author of the document.")
    parser.add_argument("--year", type=int, default=2023, help="Year of publication.")
    parser.add_argument("--type", type=str, default="document", help="Type of the document (e.g., article, thesis).")
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        raise FileNotFoundError(f"Could not find PDF at '{args.pdf_path}'")

    metadata = {
        "source": os.path.basename(args.pdf_path),
        "title": args.title,
        "author": args.author,
        "year": args.year,
        "type": args.type
    }

    print(f"Loading and splitting PDF: {args.pdf_path} ...")
    chunks = load_and_chunk(args.pdf_path, metadata)

    print(f"Embedding and merging into store ({args.store_path}) ...")
    upsert_to_store(chunks, args.store_path, args.index_name)

if __name__ == "__main__":
    main()
