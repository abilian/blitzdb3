test:
	pytest -p no:warnings --tb=short

format:
	black blitzdb tests
	isort -rc tests blitzdb

lint:
	flake8 blitzdb tests

release:
	rm -rf dist/
	python setup.py sdist
	twine upload dist/*


#
# Cleanup
#
clean:
	find . -name "*.pyc" -delete
	find . -name .DS_Store -delete
	find . -name cache -type d -delete
	find . -type d -empty -delete
	rm -rf .mypy_cache
	rm -f migration.log
	rm -rf build dist
	rm -rf *.egg .coverage
	rm -rf doc/_build
	rm -rf htmlcov

tidy: clean
	rm -rf .tox .nox
