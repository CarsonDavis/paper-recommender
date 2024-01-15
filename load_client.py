import weaviate
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

api_key = os.getenv('INFERENCE_API_KEY')
if not api_key:
    raise ValueError("No API Key found. Please set INFERENCE_API_KEY in .env file.")

client = weaviate.Client(
    url='http://localhost:8080',
    additional_headers={"X-OpenAI-Api-Key": api_key}
    )
