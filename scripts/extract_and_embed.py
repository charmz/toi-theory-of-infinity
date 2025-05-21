import boto3
import pdfplumber
import openai
from pymilvus import MilvusClient
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
s3 = boto3.client('s3')
milvus = MilvusClient(uri=os.getenv('MILVUS_URI'))

bucket = 'toi-research-bucket'
key = 'input/documents/relativity.pdf'

# Download PDF from S3
s3.download_file(bucket, key, 'relativity.pdf')

# Extract text
with pdfplumber.open('relativity.pdf') as pdf:
    text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

# Generate embedding
response = openai.Embedding.create(
    input=text,
    model="text-embedding-3-small"
)
embedding_vector = response['data'][0]['embedding']

# Insert into Milvus
milvus.insert(
    collection_name="research_documents",
    data=[{
        "embedding": embedding_vector,
        "document_name": "relativity.pdf",
        "summary": "Einstein's Relativity: Special and General Theory"
    }]
)

print("✅ Embedding stored in Milvus.")
