# magazine
django app

There is implemented  swagger UI - http://127.0.0.1:8000/doc/

API description:

POST /rest-auth/login/ - Check the credentials and return the REST Token

```bash
curl -X POST "http://127.0.0.1:8000/rest-auth/login/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: dzJluSMgGo6b1wTHoz8Cbh1wCX22i29rp8QVKXmBpfeU0TShTMKQmr6nBprIHXFL" -d "{ \"password\": \"adminadmin\", \"email\": \"admin@admin.com\", \"username\": \"None\"}"
response:
{
  "key": "752d4f5170deee6575670ae714113b8052a38a39"
}
```

- GET /api/posts/approved/  - list of approved posts
-


- GET /api/posts/ - list of the all posts
```bash
curl -X GET "http://127.0.0.1:8000/api/posts/" -H "accept: application/json" -H "X-CSRFToken: mZvSK61pHqsv4iiOxpFFFWW6iJRfSECupYcYSYdSPyzy8DeWe1khRepfDvTwVxVr"
[
  {
    "id": 1,
    "title": "1 PostAdmin",
    "body": "up vote\r\n14\r\ndown vote\r\nSin,
    "created": "2018-07-04T19:21:39.439495Z",
    "author": 2,
    "approved": false
  },
  {
    "id": 2,
    "title": "2 dfg dfg fdgdfg",
    "body": "Django - ForeignField initial value",
    "created": "2018-07-04T19:22:03.618072Z",
    "author": 2,
    "approved": true
  }
]
```

- GET /api/posts/<pk>

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/posts/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true,
    }
]
Code 200 OK
```
- POST /api/posts/ - create a post
```
curl -X POST "http://127.0.0.1:8000/api/posts/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: rsWRY8ClnduwqEYtMODfwwTen2h2roKdR3YbkoWo4ijCOafES3HrvCWrZvH6UFXa" -d "{ \"approved\": true, \"title\": \"string11243\", \"author\": 1, \"body\": \"qqqqqqqqqqqqqqqq tesrrrrrrrrrrrrr\"}"
Response body
{
  "id": 3,
  "title": "string11243",
  "body": "qqqqqqqqqqqqqqqq tesrrrrrrrrrrrrr",
  "created": "2018-07-05T09:15:16.732618Z",
  "author": 1,
  "approved": true
}
```


- PUT /rest-auth/user/ create a new user:

```
curl -X PUT "http://127.0.0.1:8000/rest-auth/user/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: mZvSK61pHqsv4iiOxpFFFWW6iJRfSECupYcYSYdSPyzy8DeWe1khRepfDvTwVxVr" -d "{ \"date_of_birth\": \"2012-10-11\", \"role\": \"2\", \"is_admin\": true, \"is_active\": true, \"email\": \"new@example.com\", \"is_staff\": false,\"name\":\"None\"}"{
	
Response body- 
{
  "email": "admin@admin.com",
  "role": 2,
  "date_of_birth": "2012-10-11",
  "is_active": true,
  "is_staff": true,
  "is_admin": true
}
Code 200 OK
```
- GET /rest-auth/user/ - get current user profile
 
```bash
curl -X GET "http://127.0.0.1:8000/rest-auth/user/" -H "accept: application/json" -H "X-CSRFToken: dzJluSMgGo6b1wTHoz8Cbh1wCX22i29rp8QVKXmBpfeU0TShTMKQmr6nBprIHXFL"
Response body
{
  "email": "admin@admin.com",
  "role": 1,
  "date_of_birth": "1201-12-12",
  "is_active": true,
  "is_staff": true,
  "is_admin": true
}
Code 200 OK
```
