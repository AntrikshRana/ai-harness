from app.harness.validator import Validator

def test_validator():
    validator = Validator()
    
    result = validator.validate("hello world")
    
    assert result is True
    
def test_empty_response():
    validator = Validator()
    
    result = validator.validate("")
    
    assert result is False

def test_whitespace_response():
    validator = Validator()
    
    result = validator.validate("       ")
    
    assert result is False
