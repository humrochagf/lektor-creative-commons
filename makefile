# Makefile

.PHONY: translations
translations: # run update translations command
	./bin/update_translations.sh

.PHONY: build
build: # build package for distribution
	rm -rf dist
	python setup.py sdist
	python setup.py bdist_wheel --universal

.PHONY: publish
publish: # publish package to the PyPI
	twine upload dist/*

.PHONY: clean
clean: # remove temporary files and artifacts
	rm -rf site/
	rm -rf *.egg-info dist build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.coverage' -exec rm -f {} +
	find . -name '__pycache__' -exec rmdir {} +
