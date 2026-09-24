import os
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv


load_dotenv()

HF_TOKEN = os.getenv("HUGGING_FACE_API_KEY")
HF_MODEL = os.getenv("HF_MODEL")


client = InferenceClient(
    api_key=HF_TOKEN,
    provider="hf-inference"
)

def create_embeddings(text):
    response = client.feature_extraction(
        text,
        model=HF_MODEL
    )


    return response
