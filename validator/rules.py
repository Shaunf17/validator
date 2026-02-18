from typing import Any
from .errors import ValidationError

class Rule:
    def validate(self, value: Any) -> None:
        raise NotImplementedError


class Required(Rule):
    def validate(self, value: Any) -> None:
        if value is None:
            raise ValidationError("Value is required")


class MinLength(Rule):
    def __init__(self, length: int):
        self.length = length

    def validate(self, value: Any) -> None:
        if not isinstance(value, str):
            raise ValidationError("Value must be a string")
        if len(value) < self.length:
            raise ValidationError(f"Minimum length is {self.length}")
