from models.triggers import *
from models import Machine


fsm = Machine(
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
    trigger=TriggerJK()
)

print(fsm.machine)
print(fsm.structural_machine)
print(fsm.memory_machine)

print(fsm.get_tables_exits())
print(fsm.get_tables_memory())
