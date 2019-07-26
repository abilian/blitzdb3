test:
	pytest -p no:warnings --tb=short

format:
	isort -a  "from __future__ import absolute_import, print_function, unicode_literals" \
                -rc tests blitzdb
	black blitzdb tests
	isort -rc tests blitzdb

lint:
	flake8 blitzdb tests
