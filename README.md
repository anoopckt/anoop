# EHR Q&A Agent Challenge
# Problem Statement
Build an intelligent Electronic Health Records (EHR) Question & Answer system using Retrieval-Augmented Generation (RAG) in Python. Your system should enable healthcare professionals to query patient records using natural language and receive accurate, context-aware responses.
# Background
Electronic Health Records contain critical patient information scattered across various documents. Healthcare professionals need quick access to specific patient data without manually searching through extensive records. Your task is to build a RAG-based system that can:
Index and retrieve information from unstructured EHR data
Answer specific queries about patient history, diagnoses, and lab results
Handle follow-up questions with contextual awareness
Provide a user-friendly interface for healthcare workers
# Data Setup
1.1 Repository Initialization
Create a GitHub repository for your project
Download the synthetic EHR dataset from: Cynthia Synthetic EHR Records
Store the dataset in a /data directory at the project root

# RAG Pipeline Implementation
Document Processing
Vector Store & Retrieval
Query Handling


# Project Structure
Your repository should follow this structure:
ehr-qa-agent/
│
├── data/                          # Contains unstructured EHR data
│   └── (dataset files)
│
├── create_documents.py            # Document creation from raw data
├── ehr_ingest.py                  # Vector store ingestion pipeline
├── ehr_rag_pipeline.py            # Core RAG implementation
├── app.py                         # Streamlit application
│
├── tests/                         # Test suite
│   ├── test_documents.py
│   ├── test_ingestion.py
│   └── test_rag_pipeline.py
│
├── .env.example                   # Example environment variables
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
# Run this project 
Python app.py