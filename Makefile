run:
	uvicorn app:app --reload

setup: requirements.txt
	pip install -r requirements.txt