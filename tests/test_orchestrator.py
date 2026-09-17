from app.harness.orchestrator import Orchestrator

class FakeModel():
    def generate(self,prompt):
        return "Generated response"
    
    def is_available(self):
        return True
    
class FakeTaskPlanner():
    def plan(self,prompt):
        return "coding"
    
class FakeModelRouter():
    def route(self,task_type):
        fake_model = FakeModel()
        return fake_model


def test_orchestrator():
    fake_task_planner = FakeTaskPlanner()
    fake_model_router = FakeModelRouter()
    
    orchestrator = Orchestrator(fake_task_planner,fake_model_router)
    response = orchestrator.run("Write a python function")
    
    assert response == "Generated response"


'''
    def run(self,prompt):
        fake_model = FakeModel()
    
        planner = FakeTaskPlanner()
        task = planner.plan(self.prompt)
    
        router = FakeModelRouter()
        response = router.route(task).generate()
    
        assert response == "Generated response"
'''
