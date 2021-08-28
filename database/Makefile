#target
build-mysql:
	docker build . -t mysql-image

start-mysql:
	docker run --name mysql-dev --env="MYSQL_ROOT_PASSWORD=root_password" -dp 3306:3306 mysql-image

v-start-mysql:
	docker run --name mysql-dev --env="MYSQL_ROOT_PASSWORD=root_password" -dp 3306:3306 --network=mysql-net --mount type=bind,src=/$$(pwd)/db_dev,dst=/var/lib/mysql mysql-image

#v-start-mysql:
#	docker run --name mysql-dev --env="MYSQL_ROOT_PASSWORD=root_password" -dp 3306:3306 --mount type=bind,src=/$$(pwd)/scripts,dst=/docker-entrypoint-initdb.d/ --mount type=bind,src=/$$(pwd)/db_dev,dst=/var/lib/mysql mysql-image

stop-mysql:
	docker rm -f mysql-dev

restart-mysql:
	$(MAKE) stop-mysql
	$(MAKE) start-mysql

inside-mysql:
	docker exec -it mysql-dev mysql -uroot -proot_password

import-db:
	docker exec -i mysql-dev mysql -u root -proot_password "CREATE DATABASE todo_db;"
	docker exec -i mysql-dev mysql -u root -proot_password "USE todo_db;"
	docker exec -i mysql-dev mysql -u root -proot_password  "SOURCE todo_db.sql"
	
#ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

copy-db-exp:
#iz containerja kopira datoteko sql - export 
	docker cp mysql-dev:todo_db.sql .