from pprint import pprint

from utils import (
    Multiplexor,
    MultiplexorCountInput,
    RowPlaceholder
)

from variants import (
    variants,
    additional_variants,
    additional_variants_func
)


mx = Multiplexor(
    count_input=MultiplexorCountInput.eight,
    row_placeholder=RowPlaceholder()
)

for ready_result, calculation_result in variants:
    mx.row_placeholder = ready_result
    first = mx.inputs.dump()
    mx.row_placeholder = calculation_result
    second = mx.inputs.dump()
    print("========================================", "MX: Based on the results of the function", sep="\n")
    pprint(first, sort_dicts=False)
    print("========================================", "MX: By function", sep="\n")
    pprint(second, sort_dicts=False)
    print("========================================")
    print("Results equals: ", first == second, "\n\n")


for placeholder in additional_variants:
    mx.row_placeholder = placeholder
    first = mx.inputs.dump()
    print("========================================", "MX: Based on the results of the function", sep="\n")
    pprint(first, sort_dicts=False)
    print("========================================")


for placeholder in additional_variants_func:
    mx.row_placeholder = placeholder
    first = mx.inputs.dump()
    print("========================================", "MX: By function", sep="\n")
    pprint(first, sort_dicts=False)
    print("========================================")


# Attention!! 

# mx.sign = False   // default
# first = mx.inputs.dump()
# mx.sign = True
# second = mx.inputs.dump()
# first != second
