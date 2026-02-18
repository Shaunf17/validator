from typing import Dict, Any
from .schema import validate_schema, Schema

class Validator:
    def __init__(self, schema: Schema):
        self.schema = schema

    def validate(self, payload: Dict[str, Any]) -> None:
        validate_schema(self.schema, payload)