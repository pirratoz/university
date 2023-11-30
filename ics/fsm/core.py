from triggers import (
    TriggerD,
    TriggerT,
    TriggerRS,
    TriggerJK
)


class FiniteStateMachine:
    def __init__(self) -> None:
        ...


fsm = FiniteStateMachine(
    
)

print(TriggerT().get_new_condition("0", "0"))
print(TriggerT().get_new_condition("0", "1"))
print(TriggerT().get_new_condition("1", "0"))
print(TriggerT().get_new_condition("1", "1"))