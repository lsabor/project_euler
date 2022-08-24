"""add path to sys path"""

import pytest
import time
import inspect

from maths.logs import logger


@pytest.fixture
def solve_problem():
    def solve(problem_file):
        problem = __import__(problem_file[:-3])
        answer = problem.ANSWER
        solution_func = problem.solution
        args = inspect.signature(solution_func)
        bypassed = list(args.parameters.values())[0].default
        bypass_str = " (bypassed)" if bypassed else ""
        start = time.perf_counter()
        solution = solution_func()
        end = time.perf_counter()
        solved = solution == answer
        if solved:
            print(f"success on {problem_file:50} in {end - start: 0.4f} seconds{bypass_str}")
        else:
            print(f"FAILURE on {problem_file:50} in {end - start: 0.4f} seconds{bypass_str}")
            assert solution == answer

    return solve
