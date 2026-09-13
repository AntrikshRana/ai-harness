"""
This is an interface that says, Every model class must have a generate function.

NOTE : for now generate() is empty.
"""

from abc import ABC,abstractmethod

class BaseModel(ABC):
    def _init_(self,model_name:str):
        self.model_name = model_name
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod 
    def is_available(self)->bool:
        pass 