from .models.gemini import GeminiModel
from .models.model_registry import ModelRegistry
gemini = GeminiModel()

registry = ModelRegistry()

registry.add("gemini",gemini)

response = registry.get("gemini").generate("What is nd operating system in one sentence.")

print(response)