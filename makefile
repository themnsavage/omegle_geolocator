run:
	python3 app/main.py
setup:
	pip install -r requirements.txt
tests:
	python3 -m pytest
clean:
	rm -rf test/__pycache__ app/__pycache__ .pytest_cache