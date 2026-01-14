from creat_document import split_documents, create_document
from ehr_ingest import ehr_vector_store
from ehr_rag_pipeline import rag_pipeline
import os
from dotenv import load_dotenv
load_dotenv()
file=os.getenv("FILE_PATH")
docs = create_document(file)
print(f"Total pages loaded from PDF: {len(docs)}")
docs = split_documents(docs)
print(f"Total documents created: {len(docs)}")
my_vector_store = ehr_vector_store(docs)
input_query = "What is the diagnosis of the patient?"
response = rag_pipeline(input_query, my_vector_store)
print("Response:", response)