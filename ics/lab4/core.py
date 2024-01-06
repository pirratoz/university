from pprint import pprint

from utils import (
    Bool,
    Multiplexor,
    MultiplexorCountInput,
    FillFinishedResult,
    CalculationsResult
)


# This is an example of equivalent multiplexers

# One is set using the function results
ready_results = FillFinishedResult(
    count_var=5,
    results=[0, 1, 2, 3, 4, 6, 7, 12, 16, 18, 20, 22, 28],
    bool=Bool.true
)
# The other is set by the function itself
calculations_results = CalculationsResult(
    function="!a * !b * !c + c * !d * !e + a * !b * !e + !a * !b * d"
)

mx = Multiplexor(
    count_input=MultiplexorCountInput.four,
    row_generator=ready_results
)

print("========================================")
print("MX: Based on the results of the function")
pprint(mx.inputs.dump())
print("========================================")
mx.row_generator = calculations_results
print("MX: By function")
pprint(mx.inputs.dump())
print("========================================")
