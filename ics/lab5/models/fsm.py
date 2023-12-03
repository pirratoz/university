class Fsm:
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]],
        exits: list[list[str]]
    ) -> None:
        self.headers = headers
        self.inputs = inputs
        self.states = states
        self.exits = exits

    def __str__(self) -> str:
        return f"[\n  headers = {self.headers}\n  inputs = {self.inputs}\n  states = {self.states}\n  exits = {self.exits}\n]"

    def __repr__(self) -> str:
        return self.__str__()
