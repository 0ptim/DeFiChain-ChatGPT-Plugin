import os
from dotenv import load_dotenv
import openai

load_dotenv()

def get_embedding(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    """
    Get the embedding for a given text
    """
    results = openai.Embedding.create(input=text, model="text-embedding-ada-002")

    return results["data"][0]["embedding"]