# magazine
django application

There is implemented  swagger UI - http://127.0.0.1:8000/doc/

API description:

- POST /api/userprofile/ - create a user(and profile). Role will be defined by field 'role'. Writers has role=1, editor had role=2, supervisor has role=3. Roles are described in settings.ROLE_CHOICES.

```
curl -X PUT "http://127.0.0.1:8000/rest-auth/user/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: FnhTwnW5mAPSuU02BwoL9MVRwY7KKACCu7TuyKn6OYUvGZxcjUnEQpx00g6fSXiU" -d "{\"email\": \"admin1@admin.com\", \"password\": \"adminadmin\", \"is_admin\": true, \"date_of_birth\": \"2012-12-12\", \"is_active\": true, \"role\": \"1\"}"

Response body
{
  "id": 2,
  "password": "adminadmin",
  "last_login": "2018-07-05T11:21:22.937685Z",
  "email": "admin@admin.com",
  "role": 1,
  "date_of_birth": "2012-12-12",
  "is_active": true,
  "is_admin": true,
  "groups": [],
  "user_permissions": []
}
```

POST /rest-auth/login/ - check the credentials and return the REST Token

```bash
curl -X POST "http://127.0.0.1:8000/rest-auth/login/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: dzJluSMgGo6b1wTHoz8Cbh1wCX22i29rp8QVKXmBpfeU0TShTMKQmr6nBprIHXFL" -d "{ \"password\": \"adminadmin\", \"email\": \"admin@admin.com\", \"username\": \"None\"}"
response:
{
  "key": "752d4f5170deee6575670ae714113b8052a38a39"
}
```

- GET /api/posts/approved/  - list of approved posts only
```bash
curl -X GET "http://127.0.0.1:8000/api/posts/approved/" -H "accept: application/json" -H "X-CSRFToken: JNTH2h97CBCIPZzpPrl6pZpeJNpnP4GN7dC8DQVgu5YjsuIkiz3GAYkncYRdbKwy"
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "title": "2 dfg dfg fdgdfg",
      "body": "fdgf fdg dfg jh jk kjl klkj l kjl jkMofgdfgty bu uyadmiftyj ytijty e is a GET('mother') parameter, or leave it blank, in case there is not.\r\n\r\nI have actually 2 questions:\r\n\r\nHow to access request inside ModelAdmin?\r\nHow to define initial value for a ForeignField?\r\nIn models.py:\r\n\r\nclass Person(models.Model):\r\n    name=models.CharField()\r\n    mother=models.ForeignKey('self')\r\nIn admin.py:\r\n\r\nclass  PersonAdminForm(forms.ModelForm):\r\n    class Meta:\r\n        model = Person\r\n\r\nclass PersonAdmin(admin.ModelAdmin):\r\n    mother = request.GET.get('mother','') #don`t know how to access request\r\n\r\n    if mother != '':\r\n        form = PersonAdminForm",
      "created": "2018-07-04T19:22:03.618072Z",
      "author": 2,
      "approved": true
    },
    {
      "id": 3,
      "title": "string11243",
      "body": "qqqqqqqqqqqqqqqq tesrrrrrrrrrrrrr",
      "created": "2018-07-05T09:15:16.732618Z",
      "author": 1,
      "approved": true
    }
  ]
}

```

Search posts:
GET /api/posts/approved/ and GET /api/posts/
```
curl -X GET "http://127.0.0.1:8000/api/posts/approved/?search=Django" -H "accept: application/json" -H "X-CSRFToken: JNTH2h97CBCIPZzpPrl6pZpeJNpnP4GN7dC8DQVgu5YjsuIkiz3GAYkncYRdbKwy"
Response body
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "title": "2 dfg dfg fdgdfg",
      "body": "Django - ForeignField initial value definition in Admin\r\nAsk Question\r\nup vote\r\n3\r\ndown vote\r\nfavorite\r\n1\r\nI have a Persons Model, which has a Mother Foreign Field to itself. When the user go to the 'add' admin form, I want to define a initial value for Mother, in case there is a GET('mother') parameter, or leave it blank, in case there is not.\r\n\r\nI have actually 2 questions:\r\n\r\nHow to access request inside ModelAdmin?\r\nHow to define initial value for a ForeignField?\r\nIn models.py:\r\n\r\nclass Person(models.Model):\r\n    name=models.CharField()\r\n    mother=models.ForeignKey('self')\r\nIn admin.py:\r\n\r\nclass  PersonAdminForm(forms.ModelForm):\r\n    class Meta:\r\n        model = Person\r\n\r\nclass PersonAdmin(admin.ModelAdmin):\r\n    mother = request.GET.get('mother','') #don`t know how to access request\r\n\r\n    if mother != '':\r\n        form = PersonAdminForm",
      "created": "2018-07-04T19:22:03.618072Z",
      "author": 2,
      "approved": true
    }
  ]
}

```


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

- GET /api/posts/<pk> - get one post

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

- POST /api/posts/ - create a post (only writers allowed to create, despite will return 405 or 400 status)
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


- POST /rest-auth/user/ - create a new user:

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
- GET /rest-auth/user/<id> - get user profile details by id
 
```bash
curl -X GET "http://127.0.0.1:8000/api/userprofile/1/" -H "accept: application/json" -H "X-CSRFToken: JNTH2h97CBCIPZzpPrl6pZpeJNpnP4GN7dC8DQVgu5YjsuIkiz3GAYkncYRdbKwy"
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

- GET /api/writerposts/{id}/ - get all posts for writer
