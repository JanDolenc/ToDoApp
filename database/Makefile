#target
build-mysql:
	docker build . -t mysql-image

start-mysql:
	docker run --name mysql-dev --env="MYSQL_ROOT_PASSWORD=root_password" -dp 3306:3306 --network=mysql-net --mount type=bind,src=/$$(pwd)/db_dev,dst=/var/lib/mysql mysql-image

stop-mysql:
	docker rm -f mysql-dev

restart-mysql:
	$(MAKE) stop-mysql
	$(MAKE) start-mysql

inside-mysql:
	docker exec -it mysql-dev mysql -uroot -proot_password
