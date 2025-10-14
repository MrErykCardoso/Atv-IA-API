from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def gen_text(prompt: str) -> str:
    try:
        client = genai.Client(api_key = GEMINI_API_KEY)
        response = client.models.generate_content(
            model = "gemini-2.5-flash", 
            contents = prompt
        )
        
        return response.text
    
    except Exception as e:
        print("⚠️ Erro de comunicação com a API:\n", e)
        return "Falha de conexão com a IA."