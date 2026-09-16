from app.models.gemini import GeminiModel
from app.models.model_registry import ModelRegistry
gemini = GeminiModel()

registry = ModelRegistry()

registry.add("gemini",gemini)

response = registry.get("gemini").generate("What is an operating system in one sentence.")

print(response)