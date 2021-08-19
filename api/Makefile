#target
build-fastapi:
	docker build . -t fastapi-image

start-fastapi:
	docker run --name fastapi-dev -v $$(pwd)/app:/app -dp 8001:80 fastapi-image /start-reload.sh

stop-fastapi:
	docker rm -f fastapi-dev

restart-fastapi:
	$(MAKE) stop-fastapi
	$(MAKE) start-fastapi