test-modules:
	pipenv run pytest tests/module_tests

test-answers:
	pipenv run pytest tests/answers_tests/$(group)