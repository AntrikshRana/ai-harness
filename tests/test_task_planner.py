from app.models.base_model import BaseModel
from app.harness.task_planner import TaskPlanner

import pytest

class FakeModel(BaseModel):
    
    def __init__(self,response):
        self.response = response
    
    def generate(self,prompt: str) ->str :
        return self.response
    
    def is_available(self) -> bool :
        return True
    

def test_task_planner():
    fake_gemini = FakeModel("coding")
    
    planner = TaskPlanner(fake_gemini)
    
    task = planner.plan("Code Dijkstra Algorithm")
    
    assert task == "coding","Task is not coding"
    
def test_invalid_task():
    fake_gemini = FakeModel("translation")
    
    planner = TaskPlanner(fake_gemini)
    
    
    with pytest.raises(ValueError):
        planner.plan("How's the weather today")
        
def test_task_planner_strips_response():
    fake_gemini = FakeModel("coding\n")
    
    planner = TaskPlanner(fake_gemini)
    
    response = planner.plan("Remove whiteapaces")
    
    assert response == "coding"
    
def test_task_planner_normalizes_response():
    fake_gemini = FakeModel("CODING")
    
    planner = TaskPlanner(fake_gemini)
    
    reponse = planner.plan("Uppercase return")
    
    assert reponse == "coding"