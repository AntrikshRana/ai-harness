from .harness.model_router import ModelRouter
from .models.model_registry import ModelRegistry
from .models.gemini import GeminiModel

gemini = GeminiModel()

registry = ModelRegistry()
registry.add("gemini",gemini)

router = ModelRouter(registry)

model = router.route("reasoning")

response = model.generate("What is an operating system in one sentence.")
print(response)