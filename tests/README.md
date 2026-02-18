# Validator

A lightweight rule-based validation library for Python.

## Example

```python
from validator.core import Validator
from validator.rules import Required, MinLength

schema = {
    "username": [Required(), MinLength(3)]
}

Validator(schema).validate({"username": "user123"})
