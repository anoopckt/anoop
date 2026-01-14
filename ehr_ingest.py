from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from creat_document import split_documents, create_document
import os
from dotenv import load_dotenv
load_dotenv()   

def ehr_vector_store(documents):
    try:
        embedding = GoogleGenerativeAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"),api_key=os.getenv("API_KEY"))
        print("Creating vector store...",embedding)
        vector_store = FAISS.from_documents(documents, embedding)
        return vector_store
    except Exception as e:
        print(f"Error creating vector store: {e}")
   