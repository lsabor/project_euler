import pytest
from inspect import signature


@pytest.fixture(scope="session")
def output_or_error():
    """evaluates a func if input maps to xoutput or raises error
    if xoutput is an error class"""

    def evaluate_function(func, input, xoutput):
        if len(signature(func).parameters) == 1:
            input = (input,)
        if type(xoutput) == type and isinstance(xoutput(), Exception):
            with pytest.raises(xoutput):
                func(*input)
        else:
            assert func(*input) == xoutput

    return evaluate_function
