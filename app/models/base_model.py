"""
This is an interface that says, Every model class must have a generate function.

NOTE : for now generate() is empty
"""

from abc import ABC,abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass