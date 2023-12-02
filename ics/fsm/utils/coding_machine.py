from math import log2, ceil

from utils.models import (
    StructuralMachine,
    MemoryExcitation
)

from triggers import Trigger


class Vector:
    def __init__(self, elements: list[str], designation: str) -> None:
        self.designation = designation
        self.values = elements
        self.size = self.__get_vector_size(len(elements))
        self.binary_map =  self.__get_vector_data(self.size, elements)
    
    @property
    def string(self) -> str:
        return ''.join(map(
            lambda i: f"{self.designation}{i}",
            range(1, self.size + 1)
        ))
    
    @staticmethod
    def __get_vector_size(count_unique_elements: int) -> int:
        return ceil(log2(count_unique_elements))
    
    @staticmethod
    def __get_vector_data(size_vector: int, elements: list[str]) -> dict[str, str]:
        return {
            value: bin(e)[2:].rjust(size_vector, "0")
            for e, value in enumerate(elements)
        }


class CodingMachine:
    def __init__(self, states: list[str], exits: list[str], inputs: list[str]) -> None:
        self.states = Vector(states, "q")
        self.exits = Vector(exits, "y")
        self.inputs = Vector(inputs, "x")
        
        self.tabel_structural = StructuralMachine([], [], [], [])
        self.tabel_memory = MemoryExcitation([], [], [])
    
    def update_models(
        self,
        headers: list[str],
        states: list[list[str]],
        exits: list[list[str]],
        trigger: Trigger
    ) -> None:
        self.__update_structural_model(
            headers,
            states,
            exits
        )
        self.__update_memory_model(
            self.tabel_structural.headers,
            self.tabel_structural.states,
            trigger
        )

    def __update_structural_model(
        self,
        headers_: list[str],
        states_: list[str],
        exits_: list[str]
    ) -> None:
        states = [ [] for _ in range(len(states_)) ]
        exits = [ [] for _ in range(len(exits_))]
        inputs = [self.inputs.binary_map[input_] for input_ in self.inputs.values]
        headers = [self.states.binary_map[state_] for state_ in headers_]
        
        for index, line_elements in enumerate(states_):
            states[index] = [
                self.states.binary_map[value]
                for value in line_elements
            ]
        
        for index, line_elements in enumerate(exits_):
            exits[index] = [
                self.exits.binary_map[value]
                for value in line_elements
            ]

        self.tabel_structural.states = states
        self.tabel_structural.exits = exits
        self.tabel_structural.inputs = inputs
        self.tabel_structural.headers = headers
    
    def __update_memory_model(
        self,
        headers: list[str],
        states: list[list[str]],
        trigger: Trigger
    ) -> None:
        memory_excitation = [ [] for _ in range(len(self.inputs.values)) ]
        for index in range(len(self.inputs.values)):
            for old_state, new_state in zip(headers, states[index]):
                state_mem = "".join([
                    trigger.get_new_condition(old_state[i], new_state[i])
                    for i in range(len(old_state))
                ])
                memory_excitation[index].append(state_mem)
        self.tabel_memory.headers = headers
        self.tabel_memory.inputs = self.tabel_structural.inputs
        self.tabel_memory.states = memory_excitation
