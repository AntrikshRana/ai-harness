from .harness.model_router import ModelRouter
from .models.model_registry import ModelRegistry
from .models.gemini import GeminiModel

from .models.base_model import BaseModel

import pytest

# gemini = GeminiModel()
# registry.add("gemini",gemini)
# assert isinstance(model,GeminiModel),"Router did not return GeminiModel"

# To test the normal routing.
# Example : If gemini is available then call gemini
def test_normal_routing():
    registry = ModelRegistry()
    
    gemini = GeminiModel()
    registry.add("gemini",gemini)
    
    router = ModelRouter(registry)
    
    model = router.route("reasoning")
    
    assert isinstance(model,GeminiModel), "Not gemini model"

# This is a fallback test.
# If gemini is unavailable then route to the next model
def test_fallback_routing():
    registry = ModelRegistry()
    
    fake_gemini = FakeModel(False)
    fake_gpt = FakeModel(True)    
    
    registry.add("gemini",fake_gemini)
    registry.add("gpt",fake_gpt)
        
    router = ModelRouter(registry)
        
    model = router.route("reasoning")
    
    assert model is fake_gpt, "No model selected"

# When none of the models are available we need to raise the exception
def test_no_model_available():
    registry = ModelRegistry()
    
    fake_gemini = FakeModel(False)
    fake_gpt = FakeModel(False)    
    
    registry.add("gemini",fake_gemini)
    registry.add("gpt",fake_gpt)
        
    router = ModelRouter(registry)
        
    with pytest.raises(RuntimeError):
        router.route("reasoning")
    
class FakeModel(BaseModel):
    def __init__(self,available):
        self.available = available
    
    def generate(self,prompt: str) -> str:
        return "Hi im a fake model"
        
    def is_available(self) -> bool:
        return self.available
