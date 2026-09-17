# from app.harness.model_router import ModelRouter
# from app.harness.task_planner import TaskPlanner

class Orchestrator:
    def __init__(self,planner,router):
        self.router = router
        self.planner = planner
    
    def run(self,prompt):
        task = self.planner.plan(prompt)
        
        response = self.router.route(task).generate(prompt)
        
        return response
