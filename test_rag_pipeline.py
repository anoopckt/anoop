from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()

def ehr_vector_store(documents):
    try:
        embedding = GoogleGenerativeAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"),api_key=os.getenv("API_KEY"))
        print("Creating vector store...",embedding)
        vector_store = FAISS.from_documents(documents, embedding)
        return vector_store
    except Exception as e:
        print(f"Error creating vector store: {e}")
def rag_pipeline(query: str, my_vector_store):
        # Perform similarity search to retrieve relevant documents
        try:
            result=my_vector_store.similarity_search(query,k=3)
        except Exception as e:
            print(f"Error during similarity search: {e}")
            return "Sorry, I couldn't process your request at this time."
        full_text = "/n/n".join([doc.page_content for doc in result])
        
        prompt = f"""You are a helpful medical assistant. Use the following context to answer the question.
        {full_text}
        Question: {query}
        Answer:"""
    
        try:
            model = ChatGoogleGenerativeAI(
                model=os.getenv("MODEL"),
                api_key=os.getenv("API_KEY")
            )
        
            response=model.invoke(prompt)
            return response
        except Exception as e:
            print(f"Error in RAG pipeline: {e}")
        return "Sorry, I couldn't process your request at this time."


result=rag_pipeline("What is the diagnosis of the patient?",my_vector_store=ehr_vector_store)
print("RAG Response:",result)