all:	up

up:
	docker-compose --env-file ./srcs/.env -f ./srcs/docker-compose.yml up --build

down:
	docker-compose -f ./srcs/docker-compose.yml down -v

stop:
	docker-compose -f ./srcs/docker-compose.yml stop

rm:
	docker-compose -f ./srcs/docker-compose.yml rm -s -v -f
	docker volume rm srcs_postgresql
	docker volume rm srcs_esdata

clean:	rm

fclean:	stop clean

.PHONY:	all up down stop rm clean fclean
