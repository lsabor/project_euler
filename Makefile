test-modules:
	pipenv run pytest tests/module_tests

test-answers:
	pipenv run pytest tests/answer_tests/$(group)

tc:
	pipenv run pytest -rA -m current
