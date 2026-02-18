from typing import Dict, List, Any
from .rules import Rule

Schema = Dict[str, List[Rule]]

def validate_schema(schema: Schema, payload: Dict[str, Any]) -> None:
    for field, rules in schema.items():
        value = payload.get(field)
        for rule in rules:
            rule.validate(value)
