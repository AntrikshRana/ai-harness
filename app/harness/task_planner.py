from app.models.base_model import BaseModel

class TaskPlanner:
    def __init__(self,model):
        self.model = model
        self.task_types = ['coding','reasoning','data_analysis']
        
    def plan(self,prompt):
        instruction = f"""
        Classify the following user request into exactly one of:
        reasoning, coding, data_analysis.
        
        Return only task type
        
        {prompt}
        """
        response = self.model.generate(instruction).strip().lower()
        
        if response in self.task_types:
            return response
        else:
            raise ValueError(f"Invalid task type: {response}")