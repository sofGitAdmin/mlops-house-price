test:
	pytest

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

lint:
	ruff check .
