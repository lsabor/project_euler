"""tests for special sequences"""

import pytest

from maths.sequences import (
    IntsSeq,
    PrimesSeq,
    TriangleNumbers,
    Fibonacci,
)


@pytest.fixture
def ints_sequence():
    return IntsSeq(name="test_ints_sequence")


@pytest.fixture
def primes_sequence():
    sequence = PrimesSeq(name="test_primes_sequence")
    yield sequence
    sequence.destroyCache()


@pytest.fixture
def triangle_numbers():
    return TriangleNumbers(name="test_triangle_numbers")


@pytest.fixture
def fibonacci():
    return Fibonacci(name="test_fibonacci")


class Test_IntsSeq:
    """tests for IntsSeq"""

    def test_initiate(self):
        IntsSeq()

    def test_values(self, ints_sequence):
        assert ints_sequence[:10] == [0, 1, -1, 2, -2, 3, -3, 4, -4, 5]
        assert ints_sequence.isInSet(190329480)
        assert ints_sequence.isInSet(3.0)
        assert not ints_sequence.isInSet("1")
        assert not ints_sequence.isInSet(0.5)


class Test_PrimesSeq:
    """tests for PrimesSeq"""

    def test_initiate(self):
        PrimesSeq()

    def test_values(self, primes_sequence):
        assert primes_sequence.readCache() == [2]
        assert primes_sequence[:9] == [2, 3, 5, 7, 11, 13, 17, 19, 23]
        assert primes_sequence.readCache() == [2, 3, 5, 7, 11, 13, 17, 19, 23]
        assert primes_sequence.takeWhileLT(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes_sequence.isInSet(1122004669637)
        assert not primes_sequence.isInSet(1122004669633)


class Test_TriangleNumbers:
    """tests for TriangleNumbers"""

    def test_initiate(self):
        TriangleNumbers()

    def test_values(self, triangle_numbers):
        assert triangle_numbers[:9] == [1, 3, 6, 10, 15, 21, 28, 36, 45]
        assert triangle_numbers.isInSet(22116304770)
        assert not triangle_numbers.isInSet(22116304775)


class Test_Fibonacci:
    """tests for Fibonacci"""

    def test_initiate(self):
        Fibonacci()

    def test_values(self, fibonacci):
        assert fibonacci[:9] == [1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert not fibonacci.isInSet(573147844013817084100)
        assert fibonacci.isInSet(573147844013817084101)
        assert not fibonacci.isInSet(573147844013817084102)
