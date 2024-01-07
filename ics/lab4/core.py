from pprint import pprint

from utils import (
    Bool,
    Multiplexor,
    MultiplexorCountInput,
    ReadyResultsPlaceholder,
    CalculatedResultsPlaceholder
)


# This is an example of equivalent multiplexers

# One is set using the function results
ready_results = ReadyResultsPlaceholder(
    count_var=5,
    results=[0, 1, 2, 3, 4, 6, 7, 12, 16, 18, 20, 22, 28],
    bool=Bool.true
)
# The other is set by the function itself
calculations_results = CalculatedResultsPlaceholder(
    function="!a * !b * !c + c * !d * !e + a * !b * !e + !a * !b * d"
)

mx = Multiplexor(
    count_input=MultiplexorCountInput.four,
    row_generator=ready_results
)

first = mx.inputs.dump()
mx.row_generator = calculations_results
second = mx.inputs.dump()

print("========================================")
print("MX: Based on the results of the function", first)
print("========================================")
print("MX: By function", second)
print("========================================")
print("Results equals: ", first == second)

# Attention!! 

# mx.sign = False   // default
# first = mx.inputs.dump()
# mx.sign = True
# second = mx.inputs.dump()
# first != second
