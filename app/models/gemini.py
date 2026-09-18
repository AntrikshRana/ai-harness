import os
from dotenv import load_dotenv
from google import genai

from .base_model import BaseModel

load_dotenv()

class GeminiModel(BaseModel):
    def __init__(self):
        super().__init__("gemini")
        self.client = genai.Client(
            api_key = os.getenv("GEMINI_API_KEY")
        )
        
    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = prompt
        )
        return response.text
    
    def is_available(self) -> bool:
        if(os.getenv("GEMINI_API_KEY")):
            return True
        
        return False