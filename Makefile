setup: requirements.txt
	pip install -r requirements.txt

run:
	uvicorn app:app --reload

test:
	python -m pytest
