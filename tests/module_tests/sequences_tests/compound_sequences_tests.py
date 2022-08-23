"""tests for compound sequences"""

import pytest

from maths.sequences.compound import PrimeFactorSeq, DivisorSeq, Counter


@pytest.fixture
def prime_factor_sequence():
    sequence = PrimeFactorSeq(name="test_prime_factor_sequence")
    yield sequence
    sequence.destroyCache()


@pytest.fixture
def divisor_sequence():
    sequence = DivisorSeq(name="test_divisor_sequence")
    yield sequence
    sequence.destroyCache()


class Test_PrimeFactorSeq:
    """tests for PrimeFactorSeq"""

    def test_initiate(self):
        PrimeFactorSeq()

    def test_values(self, prime_factor_sequence):
        assert prime_factor_sequence.readCache() == [Counter()]
        assert prime_factor_sequence[6:10] == [
            Counter({2: 1, 3: 1}),
            Counter({7: 1}),
            Counter({2: 3}),
            Counter({3: 2}),
        ]
        assert prime_factor_sequence.readCache() == [
            Counter(),
            Counter(),
            Counter({2: 1}),
            Counter({3: 1}),
            Counter({2: 2}),
            Counter({5: 1}),
            Counter({2: 1, 3: 1}),
            Counter({7: 1}),
            Counter({2: 3}),
            Counter({3: 2}),
        ]
        assert prime_factor_sequence.takeWhile(lambda x, y: len(x) < 2) == [
            Counter(),
            Counter(),
            Counter({2: 1}),
            Counter({3: 1}),
            Counter({2: 2}),
            Counter({5: 1}),
        ]
        assert prime_factor_sequence.isInSet(Counter({5: 1, 7: 23, 13: 2}))
        assert not prime_factor_sequence.isInSet(Counter({4: 1, 6: 2, 8: 3}))


class Test_DivisorSeq:
    """tests for DivisorSeq"""

    def test_initiate(self):
        DivisorSeq()

    def test_values(self, divisor_sequence):
        ds = divisor_sequence
        assert divisor_sequence.readCache() == [[]]
        assert divisor_sequence[6:10] == [[1, 2, 3, 6], [1, 7], [1, 2, 4, 8], [1, 3, 9]]
        assert divisor_sequence.readCache() == [
            [1],
            [1],
            [1, 2],
            [1, 3],
            [1, 2, 4],
            [1, 5],
            [1, 2, 3, 6],
            [1, 7],
            [1, 2, 4, 8],
            [1, 3, 9],
        ]
        assert divisor_sequence.takeWhile(lambda x, y: len(x) < 5) == [
            [1],
            [1],
            [1, 2],
            [1, 3],
            [1, 2, 4],
            [1, 5],
            [1, 2, 3, 6],
            [1, 7],
            [1, 2, 4, 8],
            [1, 3, 9],
            [1, 2, 5, 10],
            [1, 11],
        ]
        assert divisor_sequence.isInSet([1, 2, 3, 6])
        assert not divisor_sequence.isInSet([1, 2, 3, 4, 5])
