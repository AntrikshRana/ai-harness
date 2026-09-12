class ModelRegistry:
    def __init__(self):
        self.registry = {}
        
    def add(self, name, model):
        self.registry[name] = model
        
    def get(self, name):
        return self.registry[name]