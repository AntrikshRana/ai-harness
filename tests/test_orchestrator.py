from app.harness.orchestrator import Orchestrator

class FakeModel():
    def __init__(self,response,name,available):
        self.response = response
        self.name = name
        self.available = available
    
    def generate(self,prompt):
        return self.response
    
    def is_available(self):
        return self.available
    
class FakeTaskPlanner():
    def plan(self,prompt):
        return "coding"
    
class FakeModelRouter():
    
    def __init__(self,fake_gemini,fake_gpt):
        self.fake_gemini = fake_gemini
        self.fake_gpt = fake_gpt
    
    def route(self,task_type,already_tried):
        if "gemini" in already_tried:
            return self.fake_gpt
        return self.fake_gemini

class FakeValidator:
    def validate(self,response):
        if response == "Good":
            return True
        return False

def test_orchestrator():
    fake_gemini = FakeModel("Bad","gemini",True)
    fake_gpt = FakeModel("Good","gpt",True)
    
    fake_router = FakeModelRouter(fake_gemini,fake_gpt)
    
    fake_planner = FakeTaskPlanner()
    
    fake_validator = FakeValidator()
    
    orchestrator = Orchestrator(fake_planner,fake_router,fake_validator)
    
    response = orchestrator.run("Test prompt")
    
    assert response == "Good"
