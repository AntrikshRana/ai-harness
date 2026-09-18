# from app.harness.model_router import ModelRouter
# from app.harness.task_planner import TaskPlanner

class Orchestrator:
    def __init__(self,planner,router,validator):
        self.router = router
        self.planner = planner
        self.validator = validator
    
    def run(self,prompt):
        task = self.planner.plan(prompt)
        
        already_tried = []
        
        while True:
            model = self.router.route(task,already_tried)
            already_tried.append(model.name)
            
            response = model.generate(prompt)
            valid = self.validator.validate(response)
            
            if(valid):
                return response
