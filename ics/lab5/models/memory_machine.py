from .fsm import Fsm


class MemoryMachine(Fsm):
    def __init__(self, headers: list[str], inputs: list[str], states: list[list[str]], exits: list[list[str]]) -> None:
        super().__init__(headers, inputs, states, exits)
