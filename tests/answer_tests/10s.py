"""ensuring solutions work for 00s"""

import pytest
from . import get_problem_files

section = "000-100/10s"


@pytest.mark.parametrize("problem_file", get_problem_files(section))
def test_problem(solve_problem, problem_file):
    solve_problem(problem_file)
