import requests
from config import HF_API_KEY

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
TOPICS = ["Sports", "Technology", "Business", "Politics", "Health"]

def ask_api(headline: str):
    payload = 