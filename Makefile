setup:
	python3 -m venv VENV

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		# pip install --upgrade setuptools

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203 app.py

all: install lint test