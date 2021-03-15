# Flask App Template

## Prerequisites

- [Python 3.8 or greater](https://www.python.org/downloads/)

## Setup

1. Install `pipenv` (if not already installed):

	python3 -m pip install --user pipenv

2. Create virtual environment for project:

	pipenv shell

3. Install required packages into virtual environment (including development):

	pipenv install --dev

4. Run the application (as a local development server):

	FLASK_ENV=dev python app.py
