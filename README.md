# GenAI Chatbot with RAG

# Overview

A chatbot application built using FastAPI, LangChain, and Ollama. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information before generating responses.

# Problem Statement

General-purpose LLMs may not have access to domain-specific or private information. Users need a chatbot that can answer questions using their own documents and knowledge sources.

# Proposed Solution

The chatbot uses RAG to retrieve relevant context from stored documents and provides context-aware responses through an LLM.

# Architecture

User
↓
FastAPI
↓
LangChain
↓
Retriever
↓
Vector Store
↓
nomic-embed-text Embeddings
↓
Ollama (LLM)
↓
Response

# Technologies Used

- Python
- FastAPI
- LangChain
- Ollama
- nomic-embed-text
- ChromaDB 
- Mistral

# Features

- Conversational chatbot
- Document retrieval
- Context-aware responses
- Prompt engineering
- REST API endpoints

# Future Improvements

- Authentication
- Chat history storage for conversational RAG
- Multi-document support
- Web UI
