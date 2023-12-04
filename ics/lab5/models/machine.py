from copy import deepcopy

from .fsm import Fsm
from .structural_machine import StructuralMachine
from .memory_machine import MemoryMachine
from .triggers import Trigger
from utils import (
    get_code_gray,
    fill_zero_states
)


class Machine:
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]],
        exits: list[list[str]],
        trigger: Trigger
    ) -> None:
        self.machine = Fsm(headers, inputs, states, exits)
        self.structural_machine = StructuralMachine(headers, inputs, states, exits)
        self.memory_machine = MemoryMachine([], [], [], [], self.structural_machine, trigger)
        self.trigger = trigger


    def __get_tabels_pattern(self, size_vector_func: int, vector_headers: list[str], states_or_exits: list[list[str]]) -> list[Fsm]:
        tabels = []
        size_vector_state = len(self.structural_machine.headers[0])
        size_vector_inputs = len(self.structural_machine.inputs[0])
        headers = get_code_gray(size_vector_state)

        for index_func in range(size_vector_func):
            fsm = deepcopy(self.structural_machine)
            fsm.headers = headers
            fsm.exits = []
            fill_zero_states(fsm)

            for current_index, value_header in enumerate(vector_headers):
                index_header_map = fsm.headers.index(value_header)
                for index_i in range(size_vector_inputs + 1):
                    fsm.states[index_i][index_header_map] = states_or_exits[index_i][current_index][index_func]
            tabels.append(fsm)
        
        return tabels

    def get_tables_exits(self) -> list[Fsm]:
        return self.__get_tabels_pattern(
            len(self.structural_machine.exits[0][0]),
            self.structural_machine.headers,
            self.structural_machine.exits
        )

    def get_tables_memory(self) -> list[Fsm]:
        return self.__get_tabels_pattern(
            len(self.memory_machine.states[0][0]),
            self.memory_machine.headers,
            self.memory_machine.states
        )
