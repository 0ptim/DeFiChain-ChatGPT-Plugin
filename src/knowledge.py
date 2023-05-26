import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

# The name of the collection in Qdrant
collection_name = 'DeFiChainWiki'

# Create a Qdrant client
client = QdrantClient(url=os.getenv('QDRANT_HOST'),
                      api_key=os.getenv('QDRANT_API_KEY'),
                      prefer_grpc=True)

def search_docs(vector):
    results = client.search(
        collection_name=collection_name,
        query_vector=vector,
        limit=5
    )
    return [result.payload for result in results]