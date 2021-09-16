#target
build-fastapi:
	docker build . -t fastapi-image

start-fastapi:
	docker run --name fastapi-dev -v $$(pwd)/app:/app -dp 8001:80 --network=mysql-net fastapi-image /start-reload.sh

stop-fastapi:
	docker rm -f fastapi-dev

restart-fastapi:
	$(MAKE) stop-fastapi
	$(MAKE) start-fastapi

rebuild-fastapi:
	$(MAKE) build-fastapi
	$(MAKE) stop-fastapi
	$(MAKE) start-fastapi
