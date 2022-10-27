"""tests for Special Sets"""


import pytest

from maths.sets import Ints, Naturals, Primes, PrimeFactorizations
from collections import Counter


@pytest.fixture
def ints():
    return Ints()


@pytest.fixture
def naturals():
    return Naturals()


@pytest.fixture
def primes():
    return Primes()


@pytest.fixture
def primefactorizations():
    return PrimeFactorizations()


class TestInts:
    """Testing set of Ints"""

    # create Ints
    def test_instantiate(self):
        Ints()

    # is in set
    @pytest.mark.parametrize(
        "value,xinset",
        [
            (0, True),
            (1, True),
            (-1, True),
            (5, True),
            (True, True),
            (False, True),
            (12.5, False),
            ("1", False),
            ("12.5", False),
            ("", False),
        ],
    )
    def test_isinset(self, ints, value, xinset):
        assert ints.isInSet(value) == xinset


class TestNaturals:
    """Testing set of Naturals"""

    # create Naturals
    def test_instantiate(self):
        Naturals()

    # is in set
    @pytest.mark.parametrize(
        "value,xinset",
        [
            (0, True),
            (1, True),
            (5, True),
            (True, True),
            (False, True),
            (-1, False),
            (12.5, False),
            ("1.000", False),
            ("12.5", False),
            ("", False),
        ],
    )
    def test_isinset(self, naturals, value, xinset):
        assert naturals.isInSet(value) == xinset


class TestPrimes:
    """Testing set of Primes"""

    # create Primes
    def test_instantiate(self):
        Primes()

    # is in set
    @pytest.mark.parametrize(
        "value,xinset",
        [
            (0, False),
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (2677, True),
            (2049, False),
            (1373563, True),
            (1373565, False),
            (9080213, True),
            (9080191, False),
            (25326023, True),
            (25326001, False),
            (3215031767, True),
            (3215031751, False),
            (4759123151, True),
            (4759123141, False),
            (1122004669637, True),
            (1122004669633, False),
            (2152302898771, True),
            (2152302898747, False),
            (3474749660401, True),
            (3474749660383, False),
            (341550071728361, True),
            (341550071728321, False),
            (3825123056546413057, True),
            (3825123056546413051, False),
            (318665857834031151167483, True),
            (318665857834031151167461, False),
            ("2", False),
            (-1, False),
            (2.5, False),
        ],
    )
    def test_isinset(self, primes, value, xinset):
        assert primes.isInSet(value) == xinset


class TestPrimeFactorizations:
    """Testing set of PrimeFactorizations"""

    # create PrimeFactorizations
    def test_instantiate(self):
        PrimeFactorizations()

    # is in set
    @pytest.mark.parametrize(
        "value,xinset",
        [
            (Counter([]), True),
            (Counter([2, 2]), True),
            (Counter([2, 3, 5]), True),
            (Counter([4]), False),
            (Counter([-1, -1]), False),
            (Counter([1, 2, 3, 4, 5]), False),
            (Counter([5780203]), False),
            ([2, 2], False),
        ],
    )
    def test_isinset(self, primefactorizations, value, xinset):
        assert primefactorizations.isInSet(value) == xinset
