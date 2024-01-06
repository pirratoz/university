from enum import Enum
from dataclasses import dataclass


class Alphabet:
    air = ""
    parenthesis = "()"
    vars = "abcde"
    action = "+*"
    space = " "
    neg = "!"


class Bool(Enum):
    true = 1
    false = 0

    @staticmethod
    def get(integer: str | int) -> "Bool":
        return Bool.true if integer == "1" else Bool.false


@dataclass
class TabelRow:
    variables: list[Bool]
    result: Bool

    @property
    def get_string_vars(self) -> list[str]:
        return [
            f"{Alphabet.air if bool == Bool.true else Alphabet.neg}{Alphabet.vars[index]}"
            for index, bool in enumerate(self.variables)
        ]


@dataclass
class TabelFunction:
    rows: list[TabelRow]

    def dump(self) -> dict[str, list[list[str]]]:
        return {
            str(index): [
                [str(var.value) for var in row.variables],
                [str(row.result.value)]
            ]
            for index, row in enumerate(self.rows)
        }
