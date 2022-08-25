"""tests for graphs"""

import pytest

from maths.graphs import *


class Test_Helpers:
    """tests helper fxns in primes.py"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ],
    )
    def test_nodify(self, output_or_error, input, xoutput):
        output_or_error(
            lambda x: [[node.value for node in row] for row in nodify(x)], input, xoutput
        )


# TODO: finish graph tests
