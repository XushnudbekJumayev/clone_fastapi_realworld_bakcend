ve:
	python3 -m venv .ve; \
	source .ve/bin/activate; \
	pip install -r requirements.txt

docker-build:
	docker-compose up -d --build

docker-build-postgres:
	docker-compose up -d postgres --build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-restart:
	docker-compose stop
	docker-compose up -d

docker-logs:
	docker-compose logs --tail=100 -f

runserver:
	uvicorn conduit.app:app --host 0.0.0.0

runserver-dev:
	export APP-ENV=dev && uvicorn conduit.app:app --host 0.0.0.0 --reload
