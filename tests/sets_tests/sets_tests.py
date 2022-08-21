"""tests for Sets"""

import pytest

from maths.sets import Set, Cardinalities, Cardinality


@pytest.fixture
def default_set():
    return Set()


@pytest.fixture
def cardinalities():
    return Cardinalities()


class TestSet:
    """Testing of class Set"""

    # create a set
    def test_instantiate(self):
        Set()

    # represent a set
    def test_repr(self, default_set):
        assert repr(default_set)

    # assert default types
    def test_defaults(self, default_set):
        assert default_set.name == "Set"
        assert default_set.example == "A collection of literally anything"
        assert default_set.ordered is False
        assert default_set.indexed is False
        assert default_set.cardinality is None
        assert default_set.cyclic is False
        assert default_set.cached is False

    # can't order unordered sets
    def test_compare_unordered_sets_fails(self):
        S1 = Set()
        S1.ordered = False
        with pytest.raises(TypeError):
            S1 == S1

    # bool of empty set is False
    def test_bool(self, default_set):
        assert bool(default_set) is False

    # len of empty set is 0
    def test_len(self, default_set):
        assert len(default_set) == 0

    # size is cardinality
    @pytest.mark.parametrize("cardinality", [None, Cardinality(0), Cardinality("N1")])
    def test_size(self, default_set, cardinality):
        default_set.cardinality = cardinality
        assert default_set.size() == cardinality

    # test raises error when not isInSet
    @pytest.mark.parametrize("xerror", [False, True])
    def test_test(self, mocker, default_set, xerror):
        isInSet = mocker.patch.object(default_set, "isInSet")
        isInSet.return_value = not xerror
        if xerror:
            with pytest.raises(ValueError):
                default_set.test(1)
        else:
            default_set.test(1)

    # test isInSet returns False for generic test
    def test_isInSet(self, default_set):
        for value in [None, 0, 1]:
            assert not default_set.isInSet(value)


class TestCardinalities:
    """Testing of class Cardinalities"""

    # create Cardinalities set
    def test_instantiate(self):
        Cardinalities()

    # verify in set
    @pytest.mark.parametrize(
        "value,isinset",
        [
            (0, True),
            (1, True),
            ("N", True),
            ("N0", True),
            ("N1", True),
            (Cardinality("N0"), True),
            (Cardinality(1), True),
            (-1, False),
            (0.2, False),
            ("N0.2", False),
        ],
    )
    def test_isInSet(self, cardinalities, value, isinset):
        assert cardinalities.isInSet(value) == isinset


class TestCardinality:
    """Testing of class Cardinality"""

    # create Cardinality
    def test_instantiate(self):
        Cardinality(0)

    # initializations
    @pytest.mark.parametrize(
        "cardinality,xorder,xvalue",
        [
            (0, 0, 0),
            (1, 0, 1),
            ("N", 1, -1),
            ("N0", 1, 0),
            ("N1", 1, 1),
        ],
    )
    def test_initializations(self, cardinality, xorder, xvalue):
        c = Cardinality(cardinality)
        assert c.order == xorder
        assert c.value == xvalue

    # bools
    @pytest.mark.parametrize(
        "cardinality,xbool",
        [
            (Cardinality(0), False),
            (Cardinality(1), True),
            (Cardinality("N"), True),
            (Cardinality("N0"), True),
        ],
    )
    def test_bool(self, cardinality, xbool):
        assert bool(cardinality) == xbool
