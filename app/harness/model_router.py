class modelrouter:
    def select_model(self , task_type:str)->str:
        if task_type=='coding':
            return "gpt"
        elif task_type=='reasoning':
            return "gemmini"
        elif task_type == 'data analysis':
            return  "qwen"
        else:
            return "gpt"