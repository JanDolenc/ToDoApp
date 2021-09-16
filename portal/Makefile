#target
build-nginx:
	docker build . -t nginx-image

start-nginx:
	docker run --name nginx-dev -v $$(pwd):/usr/share/nginx/html -dp 80:80 nginx-image

stop-nginx:
	docker rm -f nginx-dev

restart-nginx:
	$(MAKE) stop-nginx
	$(MAKE) start-nginx
