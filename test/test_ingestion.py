from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from creat_document import split_documents, create_document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()  
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

def ehr_vector_store(documents):
    try:
        embedding = GoogleGenerativeAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"),api_key=os.getenv("API_KEY"))
        print("Creating vector store...",embedding)
        try:    
           vector_store = FAISS.from_documents(documents, embedding)
        except Exception as e:
           print(f"Error creating FAISS vector store: {e}")
           return None   

        return vector_store
    except Exception as e:
        print(f"Error creating vector store: {e}")
# documents=create_document(os.getenv("FILE_PATH"))
# documents=split_documents(documents)   
# fais_db=ehr_vector_store(documents)
# print("fais_db",fais_db)

file=os.getenv("FILE_PATH")
docs = create_document(file) 
documents=split_documents(docs)   
fais_db=ehr_vector_store(documents)
print("fais_db",fais_db)