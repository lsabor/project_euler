"""tests for graphs"""

import pytest

from maths.graphs import *


class Test_Helpers:
    """tests helper fxns in primes.py"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ([[1, 2, 3]], [[Node(1), Node(2), Node(3)]]),
        ],
    )
    def test_nodify(self, output_or_error, input, xoutput):
        output_or_error(nodify, input, xoutput)


# TODO: finish graph tests
