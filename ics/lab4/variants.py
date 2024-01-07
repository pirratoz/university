from utils import (
    Bool,
    RowPlaceholder,
    ReadyResultsPlaceholder,
    CalculatedResultsPlaceholder
)


# This is an example of equivalent multiplexers
# One is set using the function results
# The other is set by the function itself

# 22, 25, 30
variants: list[list[RowPlaceholder]] = [
    [
        ReadyResultsPlaceholder(
            count_var=5,
            results=[0, 1, 2, 3, 4, 6, 7, 12, 16, 18, 20, 22, 28],
            bool=Bool.true
        ),
        CalculatedResultsPlaceholder(
            function="!a * !b * !c + c * !d * !e + a * !b * !e + !a * !b * d"
        )
    ],
    [
        ReadyResultsPlaceholder(
            count_var=5,
            results=[0, 4, 5, 6, 7,12,14, 15, 16, 20, 28, 30, 31],
            bool=Bool.true
        ),
        CalculatedResultsPlaceholder(
            function="!a*!b*c + !b*!d*!e+c*!d*!e+b*c*d"
        )
    ],
    [
        ReadyResultsPlaceholder(
            count_var=5,
            results=[0, 1, 2, 3, 9, 17, 19, 25, 28, 29, 30, 31],
            bool=Bool.true
        ),
        CalculatedResultsPlaceholder(
            function="!a * !b * !c + !c * !d * e + !b * !c * e + a * b * c"
        )
    ],
]