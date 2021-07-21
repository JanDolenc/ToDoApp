#target start dev
start-dev:
	docker run --name nginx-dev -v /home/jan/ToDoApp/portal:/usr/share/nginx/html -dp 80:80 nginx-image

stop-dev:
	docker rm -f nginx-dev

build-nginx:
	docker build . -t nginx-image

restart-dev:
	$(MAKE) stop-dev
	$(MAKE) start-dev