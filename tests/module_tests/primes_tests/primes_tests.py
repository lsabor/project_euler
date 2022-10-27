"""tests for primes"""

import pytest
from collections import Counter

from maths.primes import *


class Test_Helpers:
    """tests helper fxns in primes.py"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (-1, TypeError),
            (3.4, TypeError),
            (0, Counter()),
            (1, Counter()),
            (1.0, Counter()),
            (2, Counter({2: 1})),
            (15, Counter({3: 1, 5: 1})),
            (28947228, Counter({2: 2, 3: 1, 293: 1, 8233: 1})),
        ],
    )
    def test_primeFactorization(self, output_or_error, input, xoutput):
        output_or_error(primeFactorization, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (Counter({}), 1),
            (Counter({2: 3}), 8),
            (Counter({2: 3, 3: 2, 4: 1}), 288),
        ],
    )
    def test_numFromCounter(self, output_or_error, input, xoutput):
        output_or_error(numFromCounter, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 2),
            (30, 8),
            (51, 32),
            (100, 40),
        ],
    )
    def test_totient(self, output_or_error, input, xoutput):
        output_or_error(totient, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((2,), 2),
            ((2, 2), 2),
            ((2, 3), 6),
            ((3, 5, 10), 30),
            ((47, 231, 428), 4646796),
        ],
    )
    def test_lcm(self, output_or_error, input, xoutput):
        output_or_error(lcm, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            ((2,), 2),
            ((2, 2), 2),
            ((2, 3), 1),
            ((5, 10), 5),
            ((1457, 4646796, 31584), 47),
        ],
    )
    def test_gcf(self, output_or_error, input, xoutput):
        output_or_error(gcf, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (1, 1),
            (2, 2),
            (54, 8),
            (25323425, 12),
            (7776, 36),
            (24300000, 216),
        ],
    )
    def test_divisorCount(self, output_or_error, input, xoutput):
        output_or_error(divisorCount, input, xoutput)

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (1, [1]),
            (2, [1, 2]),
            (54, [1, 2, 3, 6, 9, 18, 27, 54]),
            (
                25323425,
                [
                    1,
                    5,
                    25,
                    109,
                    545,
                    2725,
                    9293,
                    46465,
                    232325,
                    1012937,
                    5064685,
                    25323425,
                ],
            ),
            (
                7776,
                [
                    1,
                    2,
                    3,
                    4,
                    6,
                    8,
                    9,
                    12,
                    16,
                    18,
                    24,
                    27,
                    32,
                    36,
                    48,
                    54,
                    72,
                    81,
                    96,
                    108,
                    144,
                    162,
                    216,
                    243,
                    288,
                    324,
                    432,
                    486,
                    648,
                    864,
                    972,
                    1296,
                    1944,
                    2592,
                    3888,
                    7776,
                ],
            ),
        ],
    )
    def test_divisors(self, output_or_error, input, xoutput):
        output_or_error(divisors, input, xoutput)
