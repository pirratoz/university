from models import Fsm


def fill_undefined_states(fsm: Fsm) -> None:
    size_line = len(fsm.headers)
    count_lines = len(fsm.states)
    fsm.states = [
        [
            "*"
            for index_ in range(size_line)
        ]
        for index in range(count_lines)
    ]
