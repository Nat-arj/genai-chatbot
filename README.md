# GenAI Chatbot with RAG

# Overview

A Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, ChromaDB, Ollama, and Mistral. The system retrieves relevant information from documents using semantic search and generates context-aware responses using a locally hosted Large Language Model (LLM).

# Problem Statement

General-purpose Large Language Models (LLMs) may not have access to domain-specific, private, or custom documents. This can lead to inaccurate responses or hallucinations when answering document-related questions.

# Proposed Solution

This project implements a Retrieval-Augmented Generation (RAG) pipeline that retrieves relevant document chunks using semantic search and provides them as context to an LLM. This improves answer accuracy and enables document-aware question answering.

# Architecture

PDF Documents 
    ↓ 
Document Loader 
    ↓ 
Text Chunking 
    ↓ 
nomic-embed-text Embeddings 
    ↓ 
ChromaDB Vector Store 
    ↓ 
Retriever 
    ↓ 
Prompt Template 
    ↓ 
Mistral (via Ollama) 
    ↓ 
Generated Response

# Technologies Used

- Python
- FastAPI
- LangChain
- Ollama
- nomic-embed-text
- ChromaDB 
- Mistral

# Features

- PDF document ingestion
- Text chunking and embedding generation
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Context-aware responses
- Prompt engineering
- FastAPI REST API backend
- Local LLM execution using Ollama

# Future Improvements

- Authentication
- Chat history storage for conversational RAG
- Multi-document support
- Web UI
