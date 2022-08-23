"""tests for sequences"""

import pytest
import os

from maths.sequences import (
    slicify,
    Sequence,
    TestOnlySequence,
    FormulaicSequence,
    InvertableSequence,
    IterativeSequence,
    InverseIterativeSequence,
)
from maths.math import sqrt


@pytest.fixture
def sequence():
    return Sequence(name="test_sequence")


@pytest.fixture
def cached_sequence():
    sequence = Sequence(name="test_cached_sequence", cached=True)
    yield sequence
    sequence.destroyCache()


@pytest.fixture
def test_only_sequence():
    class MyTOS(TestOnlySequence):
        def _isInSet(self, n):
            return n % 2 == 0

        def nextToTest(self, n):
            return n + 1

    return MyTOS(name="test_test_only_sequence")


@pytest.fixture
def formulaic_sequence():
    class MyFS(FormulaicSequence):
        def formula(self, n):
            return n**2

    return MyFS(name="test_formulaic_sequence")


@pytest.fixture
def invertable_sequence():
    class MyIFS(InvertableSequence):
        def formula(self, n):
            return n**2

        def inverseFormula(self, n):
            return sqrt(n)

    return MyIFS(name="test_invertable_sequence")


@pytest.fixture
def iterative_sequence():
    class MyIS(IterativeSequence):
        first_value = 3

        def getNext(self, n):
            return n**2 / 2

    return MyIS(name="test_iterative_sequence")


@pytest.fixture
def inverse_iterative_sequence():
    class MyIIS(InverseIterativeSequence):
        first_value = 3

        def getNext(self, n):
            return n**2 / 2

        def getPrevious(self, n):
            return sqrt(2 * n)

    return MyIIS(name="test_invertable_sequence")


class TestHelpers:
    """testing helper functions"""

    @pytest.mark.parametrize(
        "input,xoutput",
        [
            (slice(1, 6, 2), slice(1, 6, 2)),
            (5, slice(5, 6, 1)),
            (1.32, TypeError),
        ],
    )
    def test_slicify(self, output_or_error, input, xoutput):
        output_or_error(slicify, input, xoutput)


class TestSequence:
    """testing class Sequence"""

    def test_initialize(self):
        Sequence()

    def test_caching(self, cached_sequence):
        """tests basic caching operations"""
        assert os.path.exists(cached_sequence.cache_file)
        assert [] == cached_sequence.readCache()
        cached_sequence.seq = [1, 2, 3]
        cached_sequence.expandCache()
        assert [1, 2, 3] == cached_sequence.readCache()
        cached_sequence.seq += [4, 5, 6]
        cached_sequence.expandCache()
        assert [1, 2, 3, 4, 5, 6] == cached_sequence.readCache()
        cached_sequence.resetCache()
        assert [] == cached_sequence.readCache()
        # TODO
        # cached_sequence.concatenateCache([1,2,3,4])
        # assert [1,2,3,4] == cached_sequence.readCache()

    def test_getitem(self, sequence):
        sequence.seq = [0, 1, 2, 3, 4, 5]
        assert sequence[0] == 0
        assert sequence[1:3] == [1, 2]
        assert sequence[0::2] == [0, 2, 4]

    def test_iterable(self, sequence):
        sequence.seq = [0, 1, 2]
        iter_seq = iter(sequence.seq)
        assert next(iter_seq) == 0
        assert next(iter_seq) == 1
        assert next(iter_seq) == 2
        with pytest.raises(StopIteration):
            next(iter_seq)

    def test_yieldWhile(self, sequence):
        sequence.seq = [0, 1, 2, 3, 4, 5]
        iter_seq = sequence.yieldWhile(lambda x: x < 3)
        assert next(iter_seq) == 0
        assert next(iter_seq) == 1
        assert next(iter_seq) == 2
        with pytest.raises(StopIteration):
            next(iter_seq)

    def test_takeWhile(self, sequence):
        sequence.seq = [0, 1, 2, 3, 4, 5]
        assert sequence.takeWhile(lambda x, y: x <= 3) == [0, 1, 2, 3]
        assert sequence.takeWhileLT(4) == [0, 1, 2, 3]


class Test_TestOnlySequence:
    """tests for TestOnlySequence"""

    def test_initialize(self):
        TestOnlySequence()

    def test_testUpTo(self, test_only_sequence):
        test_only_sequence.seq = [0, 2, 4]
        test_only_sequence.testUpTo(1)
        assert test_only_sequence.seq == [0, 2, 4]
        test_only_sequence.testUpTo(4)
        assert test_only_sequence.seq == [0, 2, 4, 6]

    def test_getitem(self, test_only_sequence):
        test_only_sequence.seq = [0, 2, 4]
        assert test_only_sequence[-1] == 4
        assert test_only_sequence[2] == 4
        assert test_only_sequence[3] == 6
        assert test_only_sequence[:8:2] == [0, 4, 8, 12]
        assert test_only_sequence[-1] == 14


class Test_FormulaicSequence:
    """tests for FormulaicSequence"""

    def test_initialize(self):
        FormulaicSequence()

    def test_getitem(self, formulaic_sequence):
        assert formulaic_sequence[0] == 0
        assert formulaic_sequence[2] == 4
        assert formulaic_sequence[:5] == [0, 1, 4, 9, 16]


class Test_InvertableSequence:
    """tests for FormulaicSequence"""

    def test_initialize(self):
        InvertableSequence()

    def test_isInSet(self, invertable_sequence):
        assert invertable_sequence.isInSet(4)
        assert not invertable_sequence.isInSet(5)
        assert not invertable_sequence.isInSet(8)
        assert invertable_sequence.isInSet(9)

    def test_getIndex(self, invertable_sequence):
        assert invertable_sequence.getIndex(0) == 0
        assert invertable_sequence.getIndex(16) == 4

    def test_getNextPrevious(self, invertable_sequence):
        assert invertable_sequence.getNext(0) == 1
        assert invertable_sequence.getPrevious(1) == 0
        assert invertable_sequence.getNext(16) == 25
        assert invertable_sequence.getPrevious(25) == 16


class Test_IterativeSequence:
    """tests for IterativeSequence"""

    def test_initialize(self):
        IterativeSequence()

    def test_getitem(self, iterative_sequence):
        assert iterative_sequence.seq == [3]
        assert iterative_sequence[2] == 4.5 * 4.5 / 2
        assert iterative_sequence.seq == [3, 4.5, 10.125]
        assert iterative_sequence[3] == 10.125 * 10.125 / 2


class Test_InverseIterativeSequence:
    """tests for InverseIterativeSequence"""

    def test_initialize(self):
        InverseIterativeSequence()

    def test_isInSet(self, inverse_iterative_sequence):
        assert inverse_iterative_sequence.seq == [3]
        assert inverse_iterative_sequence.isInSet(10.125) == True
        assert inverse_iterative_sequence.seq == [3, 4.5, 10.125]
        assert inverse_iterative_sequence.isInSet(4.5) == True
