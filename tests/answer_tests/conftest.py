"""add path to sys path"""

import pytest
import time
import inspect

from maths.logs import logger


@pytest.fixture
def solve_problem():
    def solve(problem_file):
        start = time.perf_counter()
        problem = __import__(problem_file[:-3])
        answer = problem.ANSWER
        solution_func = problem.solution
        solution = solution_func()
        end = time.perf_counter()
        duration = end - start
        duration_str = f" (please refactor, duration over 1 sec)" if duration > 1 else ""
        solution_func_args = inspect.signature(solution_func)
        bypassed = list(solution_func_args.parameters.values())[0].default
        bypass_str = " (bypassed)" if bypassed else ""
        assert solution == answer
        print(f"success on {problem_file:50} in {duration: 0.4f} seconds{bypass_str}{duration_str}")

    return solve
