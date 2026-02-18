import pytest
from validator.core import Validator
from validator.rules import Required, MinLength
from validator.errors import ValidationError

def test_valid_payload():
    schema = {
        "username": [Required(), MinLength(3)]
    }
    validator = Validator(schema)
    validator.validate({"username": "shaun"})

def test_missing_field():
    schema = {
        "username": [Required()]
    }
    validator = Validator(schema)
    with pytest.raises(ValidationError):
        validator.validate({})
