# search_info

## About project
A little web-app which returns one question per request for a quiz.

## Requirements for Linux
- make
- docker version 20.10.14
- docker-compose version 1.25.0

## Run project
Need to call `make` (or `sudo make`). It depends on your access level for docker daemon.

## Example

##### Request
```
curl -i -X POST -H "Content-Type: application/json" 127.0.0.1:8080/posts -d '{"search":"привет"}'
```

##### Response
```
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Sun, 05 Jun 2022 19:19:40 GMT
Content-Type: application/json
Content-Length: 407
Connection: keep-alive

{"count":1,"find":"дратути","results":[{"created_date":"2019-12-21 22:32:12","post":"Всем дратути)\nНарод,как думаете,стоит ли делать такое крыло (в газетах)? Отпишите в коммы,пожалуйста,нужен совет)\nФота для примера:","rubrics":"['VK-1603736028819866', 'VK-83173127041', 'VK-38797155901']"}]}
```

##### Request
```
curl -i -X POST -H "Content-Type: application/json" 127.0.0.1:8000/posts -d '{"remove":5}'
```

##### Response
```
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Sun, 05 Jun 2022 19:21:15 GMT
Content-Type: application/json
Content-Length: 24
Connection: keep-alive

{"id":5,"removed":true}
```
