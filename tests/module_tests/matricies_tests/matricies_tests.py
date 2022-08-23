"""tests for matricies"""

import pytest

from maths.matrices import *


class Test_Helpers:
    """tests helper fxns in matricies.py"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (
                " 01 02 03\n 04 05 06\n 07 08 09",
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            ),
        ],
    )
    def test_parseMatString(self, output_or_error, input, xoutput):
        output_or_error(lambda x: parseMatString(x).tolist(), input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (
                np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                [
                    [[1, 5, 9]],
                    [[2, 6]],
                    [[4, 8]],
                    [[3]],
                    [[7]],
                    [[3, 5, 7]],
                    [[6, 8]],
                    [[2, 4]],
                    [[9]],
                    [[1]],
                ],
            )
        ],
    )
    def test_getAllDiagonals(self, output_or_error, input, xoutput):
        output_or_error(
            lambda x: list(map(lambda x: x.tolist(), getAllDiagonals(x))),
            input,
            xoutput,
        )
