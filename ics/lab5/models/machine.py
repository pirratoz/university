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


    def get_tables_exits(self) -> list[Fsm]:
        tabels = []
        size_vector_state = len(self.structural_machine.headers[0])
        size_vector_inputs = len(self.structural_machine.inputs[0])
        headers = get_code_gray(size_vector_state)

        for index_exit in range(len(self.structural_machine.exits[0][0])):
            fsm = deepcopy(self.structural_machine)
            fsm.headers = headers
            fsm.exits = []
            fill_zero_states(fsm)
            for current_index, value_header in enumerate(self.structural_machine.headers):
                index_header_map = fsm.headers.index(value_header)
                for index_i in range(size_vector_inputs + 1):
                    fsm.states[index_i][index_header_map] = self.structural_machine.exits[index_i][current_index][index_exit]
            tabels.append(fsm)
        
        return tabels

    def get_tables_memory(self) -> list[Fsm]:
        tabels = []
        size_vector_state = len(self.structural_machine.headers[0])
        size_vector_inputs = len(self.structural_machine.inputs[0])
        headers = get_code_gray(size_vector_state)

        for index_memory in range(len(self.memory_machine.states[0][0])):
            fsm = deepcopy(self.structural_machine)
            fsm.headers = headers
            fsm.exits = []
            fill_zero_states(fsm)
            for current_index, value_header in enumerate(self.memory_machine.headers):
                index_header_map = fsm.headers.index(value_header)
                for index_i in range(size_vector_inputs + 1):
                    fsm.states[index_i][index_header_map] = self.memory_machine.states[index_i][current_index][index_memory]
            tabels.append(fsm)
        
        return tabels
