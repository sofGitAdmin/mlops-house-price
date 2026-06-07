test:
	PYTHONPATH=. pytest tests/test_api.py -v

test-live:
	PYTHONPATH=. pytest tests/test_api_live.py -v
	
lint:
	ruff check .

up:
	docker compose up --build

down:
	docker compose down

logs-api:
	docker logs house-price-api --tail 100

predict:
	curl -X POST "http://localhost:8000/predict" \
	-H "Content-Type: application/json" \
	-d '{"surface":90,"rooms":4}'

ci:
	make lint
	make test
	docker build -t mlops-house-price-api .