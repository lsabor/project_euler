"""tests for math"""

import pytest

from maths.math import *


class Test_Helpers:
    """tests helper fxns in maths.py"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (0, 0),
            (4, 10),
            (100, 5050),
        ],
    )
    def test_sumConsecutiveInts(self, input, xoutput):
        assert sumConsecutiveInts(input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ([], 0),
            ([1, 2, 3], 14),
            ([5, 10, 15], 350),
            ([5, -10, 15], 350),
        ],
    )
    def test_sumSquares(self, input, xoutput):
        assert sumSquares(input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (0, 1),
            (1, 1),
            (5, 120),
            (20, 2432902008176640000),
        ],
    )
    def test_factorial(self, input, xoutput):
        assert factorial(input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((0, 0), 1),
            ((1, 0), 1),
            ((10, 8), 90),
            ((12, 7), 95040),
        ],
    )
    def test_partialFactorial(self, input, xoutput):
        assert partialFactorial(*input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((0, 0), 1),
            ((1, 0), 1),
            ((0, 1), 1),
            ((10, 8), 45),
            ((12, 7), 792),
        ],
    )
    def test_nChoosek(self, input, xoutput):
        assert nChoosek(*input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (0, 0),
            (1, 1),
            (12345, 15),
            (9736247, 38),
        ],
    )
    def test_sumOfDigits(self, input, xoutput):
        assert sumOfDigits(input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ("HI", ["HI", "IH"]),
            ("BYE", ["BYE", "BEY", "YBE", "YEB", "EBY", "EYB"]),
            ("BBE", ["BBE", "BEB", "BBE", "BEB", "EBB", "EBB"]),
        ],
    )
    def test_stringPermutations(self, input, xoutput):
        assert list(stringPermutations(input)) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((2, 5, 3), 2),
            ((2, 5, 0), 32),
            ((1, 0, 100), 1),
            ((123, 45, 1579), 191),
            ((456874563, 456967832135, 1234511), 757980),
        ],
    )
    def test_modex(self, input, xoutput):
        assert modex(*input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((2, 2, 0), 4),
            ((3, 3, 0), 7625597484987),
            ((5, 4, 12389), 11770),
        ],
    )
    def test_tetrate(self, input, xoutput):
        assert tetrate(*input) == xoutput

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ([], [()]),
            ([1], [(), (1,)]),
            ([1, 2], [(), (1,), (2,), (1, 2)]),
            ([1, 2, 3], [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]),
        ],
    )
    def test_powerset(self, input, xoutput):
        assert list(powerset(input)) == xoutput
