from copy import deepcopy

from .fsm import Fsm
from .structural_machine import StructuralMachine
from .triggers import Trigger


class MemoryMachine(Fsm):
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]],
        exits: list[list[str]],
        structural_machine: StructuralMachine,
        trigger: Trigger
    ) -> None:
        super().__init__(headers, inputs, states, exits)
        self.__update_machine(structural_machine, trigger)
    
    def __update_machine(self, structural_machine: StructuralMachine, trigger: Trigger) -> None:
        self.inputs = deepcopy(structural_machine.inputs)
        self.headers = deepcopy(structural_machine.headers)
        self.states = deepcopy(structural_machine.states)
        self.exits = deepcopy(structural_machine.exits)
        self.__update_states(trigger)
    
    def __update_states(self, trigger: Trigger) -> None:
        size_vector = len(self.headers[0])
        for index_h in range(len(self.headers)):
            for index_i in range(len(self.inputs)):
                state = ""
                for index_v in range(size_vector):
                    state += trigger.get_new_state(
                        self.headers[index_h][index_v],
                        self.states[index_i][index_h][index_v]
                    )
                self.states[index_i][index_h] = state
