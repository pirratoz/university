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
    def __init__(
        self,
        headers: list[str],
        states: list[list[str]],
        exits: list[list[str]],
        inputs: list[str],
        trigger: Trigger
    ) -> None:
        self.headers = headers
        self.states = states
        self.exits = exits
        self.inputs = inputs
        self.trigger = trigger

        self.code_machine = CodingMachine(
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

    def update_tabels(self) -> None:
        self.code_machine.update_models(
            self.headers,
            self.states,
            self.exits,
            self.trigger
        )

    def __str__(self) -> str:
        return forms.fsm_str.format(
            A = self.code_machine.states.values,
            W = self.code_machine.exits.values,
            Z = self.code_machine.inputs.values,
            I = self.code_machine.states.size,
            L = self.code_machine.inputs.size,
            N = self.code_machine.exits.size,
            IQ = self.code_machine.states.string,
            LX = self.code_machine.inputs.string,
            NY = self.code_machine.exits.string
        )


fsm = FiniteStateMachine(
    headers = [
        "a1", "a2", "a3", "a4"
    ],
    states = [
        ["a3", "a4", "a1", "a1"],
        ["a4", "a1", "a2", "a3"]
    ],
    exits = [
        ["w3", "w5", "w1", "w4"],
        ["w5", "w2", "w1", "w3"]
    ],
    inputs = [
        "z1", "z2"
    ],
    trigger=TriggerT()
)

fsm.update_tabels()

print(fsm.code_machine.tabel_structural)
print(fsm.code_machine.tabel_memory)
