# magazine
django application, Django 1.11.14, Python 3.5

There is implemented a swagger UI - http://127.0.0.1:8000/doc/ and added custom user profile - used email/password auth instead username.

# Endpoints:

- login - http://127.0.0.1:8000/rest-auth/login/
- create a user and get token - http://127.0.0.1:8000/api/userprofile 
- just get auth token - http://127.0.0.1:8000/api-token-auth/
- get approved posts - http://127.0.0.1:8000/api/posts/approved/
- search posts by string http://127.0.0.1:8000/api/posts/approved/?search=Django
- get all posts (with token auth) - http://127.0.0.1:8000/api/posts/
- get all post by writer id (with token auth) - http://127.0.0.1:8000/api/writerposts/2/

Also there is provided a test user in fixtures:
email - editor@admin.com
password - 'adminadmin'
```bash
python manage.py loaddata posts/fixtures/initial_data.json
```

Commands:
```
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py runserver
```

# API description:

- POST /api/userprofile/ - create a user(and profile). Role will be defined by field 'role'. Writers has role=1, editor had role=2, supervisor has role=3. Roles are described in settings.ROLE_CHOICES.

```
$ curl -X POST "http://127.0.0.1:8000/api/userprofile/" -H "accept: applicatdeee6575670ae714113b8052a38a39" -H "Content-Type: application/json"  -d '{ "password": "adminadmin", "email": "editor11@admin.com", "date_of_birth":"1945-01-01", "role":2}'
response:
{"id":5,"email":"editor11@admin.com","role":2,"date_of_birth":"1945-01-01","is_active":true,"is_admin":false,"groups":[],"user_permissions":[]}
```

POST /rest-auth/login/ - check the credentials and return the REST Token

```bash
curl -X POST "http://127.0.0.1:8000/rest-auth/login/" -H "accept: application/json" -H "Content-Type: application/json" -d '{ "password": "adminadmin", "email": "editor@admin.com"}'
response:
{
  "key": "752d4f5170deee6575670ae714113b8052a38a39"
}
```

- GET /api/posts/approved/  - list of approved posts only
```bash
curl -X GET "http://127.0.0.1:8000/api/posts/approved/" -H "accept: application/json" 
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
GET /api/posts/approved/ 
```
curl -X GET "http://127.0.0.1:8000/api/posts/approved/?search=Django" -H "accept: application/json"
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
curl -X GET "http://127.0.0.1:8000/api/posts/" -H "accept: application/json" -H "Authorization: Token 752d4f5170deee6575670ae714113b8052a38a39" 
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
curl -X POST "http://127.0.0.1:8000/api/posts/"-H "Authorization: Token 752d4f5170deee6575670ae714113b8052a38a39" -H "accept: application/json" -H "Content-Type: application/json" -d '{ "approved": true, "title": "string11243", "author": 1, "body": "qqqqqqqqqqqqqqqq tesrrrrrrrrrrrrr"}'
Response body, 201 code
{
  "title": "string11243",
  "body": "qqqqqqqqqqqqqqqq tesrrrrrrrrrrrrr",
  "author": 1,
  "approved": true
}
```

- GET /api/writerposts/{id}/ - get all posts for writer id
```bash
curl -X GET "http://127.0.0.1:8000/api/writerposts/2/" -H "accept: application/json" -H "Authorization: Token 752d4f5170deee6575670ae714113b8052a38a39" -d '{"pk": 2}'
response: 200 OK
{
  "id": 2,
  "email": "editor@admin.com",
  "role": 2,
  "posts": [
    "1 Post acticle",
    "2 post title article"
  ]
}

```
