from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ValidatorParms:
    """Objeto recebe os parametros da requisição"""
    password: str
    rules: list[dict[str, int]]
    
