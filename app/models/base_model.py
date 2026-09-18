"""
This is an interface that says, Every model class must have a generate function.

NOTE : for now generate() is empty.
"""

from abc import ABC,abstractmethod

class BaseModel(ABC):
    
    def __init__(self,name:str):
        self.name = name
        
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod 
    def is_available(self)->bool:
        pass 
    