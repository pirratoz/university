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

    def get_structural_machine(self) -> tuple[list[str], list[str], list[str], list[str]]:
        states = [ [] for _ in range(len(self.states)) ]
        exits = [ [] for _ in range(len(self.exits))]
        inputs = [self.code_machine.inputs.binary_map[input_] for input_ in self.inputs]
        headers = [self.code_machine.states.binary_map[state_] for state_ in self.headers]
        
        for index, line_elements in enumerate(self.states):
            states[index] = [
                self.code_machine.states.binary_map[value]
                for value in line_elements
            ]
        
        for index, line_elements in enumerate(self.exits):
            exits[index] = [
                self.code_machine.exits.binary_map[value]
                for value in line_elements
            ]

        return headers, inputs, states, exits

    def get_memory_excitation_function(
        self,
        headers: list[str],
        states: list[list[str]]
    ) -> list[list[str]]:
        memory_excitation = [ [] for _ in range(len(self.inputs)) ]
        for index in range(len(self.inputs)):
            for old_state, new_state in zip(headers, states[index]):
                state_mem = "".join([
                    self.trigger.get_new_condition(old_state[i], new_state[i])
                    for i in range(len(old_state))
                ])
                memory_excitation[index].append(state_mem)
        return memory_excitation

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

print(fsm)
print(fsm.code_machine.states.binary_map)
print(fsm.code_machine.exits.binary_map)
print(fsm.code_machine.inputs.binary_map)

headers, inputs, states, exits = fsm.get_structural_machine()
memory_function = fsm.get_memory_excitation_function(headers, states)

print(memory_function)
