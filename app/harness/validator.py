class Validator:
    def validate(self,response):
        response = response.strip()
        
        if not response:
            return False
        else:
            return True
