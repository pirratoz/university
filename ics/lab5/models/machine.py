from .fsm import Fsm
from .structural_machine import StructuralMachine
from .memory_machine import MemoryMachine
from .triggers import Trigger


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
        self.memory_machine = MemoryMachine([], [], [], [])
        self.structural_machine = StructuralMachine([], [], [], [])
        self.trigger = trigger

    def get_tables_exits(self) -> list[Fsm]:
        return []

    def get_tables_memory(self) -> list[Fsm]:
        return []
