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
            self.get_unique_values_from_list(self.states),
            self.get_unique_values_from_list(self.exits),
            self.inputs
        )

    def get_unique_values_from_list(self, iter_: list[list[str]]) -> list[str]:
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
        "a1", "a2", "a3", "a4", "a5", "a6"
    ],
    states = [
        ["a5", "a5", "a5", "a6", "a1", "a2"],
        ["a6", "a6", "a6", "a3", "a4", "a5"]
    ],
    exits = [
        ["w3", "w3", "w3", "w5", "w1", "w4"],
        ["w5", "w5", "w5", "w2", "w1", "w3"]
    ],
    inputs = [
        "z1", "z2"
    ],
    trigger=TriggerT()
)

fsm.update_tabels()

outputs = fsm.code_machine.get_Carnot_map_for_exits()

print(outputs)
