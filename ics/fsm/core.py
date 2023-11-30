from triggers import (
    Trigger,
    TriggerD,
    TriggerT,
    TriggerRS,
    TriggerJK
)
from utils.coding_machine import CodingMachine
from utils import forms


class FiniteStateMachine:
    def __init__(self, states: list[list[str]], exits: list[list[str]], inputs: list[str], trigger: Trigger) -> None:
        self.states = states
        self.exits = exits
        self.inputs = inputs
        self.trigger = trigger

        self.coding_machine = CodingMachine(
            self.get_unique_value_from_list(self.states),
            self.get_unique_value_from_list(self.exits),
            self.inputs
        )

    def get_unique_value_from_list(self, iter_: list[list[str]]) -> list[str]:
        unique = []
        for line_elements in iter_:
            for element in line_elements:
                if element not in unique:
                    unique.append(element)
        return sorted(unique)

    def __str__(self) -> str:
        return forms.fsm_str.format(
            A = self.coding_machine.A,
            W = self.coding_machine.W,
            Z = self.coding_machine.Z,
            I = self.coding_machine.I,
            L = self.coding_machine.L,
            N = self.coding_machine.N,
            IQ = self.coding_machine.get_vector_states(),
            LX = self.coding_machine.get_vector_inputs(),
            NY = self.coding_machine.get_vector_exits()
        )


fsm = FiniteStateMachine(
    states = [
        ["a2", "a2", "a1", "a1"],
        ["a4", "a3", "a4", "a4"]
    ],
    exits = [
        ["w1", "w1", "w2", "w4"],
        ["w5", "w3", "w4", "w5"]
    ],
    inputs = [
        "z1", "z2"
    ],
    trigger=TriggerT()
)

print(fsm)
