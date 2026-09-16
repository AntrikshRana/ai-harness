class ModelRouter:
    def __init__(self, registry):
        self.task_type = {
            "reasoning" : ["gemini","gpt"],
            "coding" : ["gpt","gemini"],
            "data_analysis" : ["qwen","gemini"]
        }
        self.registry = registry
        
    def route(self, task_type):
        
        if task_type not in self.task_type:
            raise ValueError(f"Unknown task type: {task_type}")
        
        for model_name in self.task_type[task_type]:
            model = self.registry.get(model_name)
            if model.is_available():
                return model
            
        raise RuntimeError("No model available")