from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
from dotenv import load_dotenv
load_dotenv()   

# Function to create documents from a PDF file
def create_document(file_path: str):
    try:
       loader = PyPDFLoader(file_path)
       documents = loader.load()
       return documents
    except Exception as e:
         print(f"Error loading document: {e}")
         return []
#Function to split documents into smaller chunks
def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    try:
       texts = text_splitter.split_documents(documents)
       return texts
    except Exception as e:
         print(f"Error splitting documents: {e}")
         texts = []
        

    
