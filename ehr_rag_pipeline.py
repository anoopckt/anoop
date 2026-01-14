# from ehr_ingest import my_vector_store
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
def rag_pipeline(query: str, my_vector_store):
        # Perform similarity search to retrieve relevant documents
        result=my_vector_store.similarity_search(query,k=3)
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
       