from dataclasses import dataclass
from enum import Enum


class MultiplexorCountInput(Enum):
    four = 4
    eight = 8
    sixteen = 16


@dataclass
class MultiplexorResultInput:
    result_zero: str
    result_one: str

    def dump(self) -> dict[str, str]:
        return {"1": self.result_one, "0": self.result_zero}


class InputHashMap:
    def __init__(self) -> None:
        self.values: dict[str, MultiplexorResultInput] = {}
    
    def __setitem__(self, key: str, value: MultiplexorResultInput):
        self.values[key] = value
    
    def dump(self) -> dict[str, dict[str, str]]:
        return {
            key: value.dump()
            for key, value in self.values.items()
        }
