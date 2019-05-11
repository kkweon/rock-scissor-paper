lint:
	pylint **/*.py

test:
	pytest


format:
	isort -y
	black .
