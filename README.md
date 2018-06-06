# python-user-service-example
A Web Service example using Python (Flask-RESTful, Flask-SQLAlchemy) and Docker.

# Usage
To build the docker images (service and DB):
```
$ docker-compose build
```

To get the service and DB running:
```
$ docker-compose up
```

Before running the set up DB commands, create a `user` DB locally:
```
$ mysql -h 127.0.0.1 -u root -p -e "create database user";
```

To set up the DB:
```
$ docker-compose run service-user python manage.py db init
$ docker-compose run service-user python manage.py db migrate
$ docker-compose run service-user python manage.py db upgrade
```

This following commands install new dependencies:
```
$ docker exec service-user pip install <package>
$ docker exec service-user pip freeze
$ docker exec service-user pip install -r requirements.txt
```

To get everything down:
```
$ docker-compose stop
$ docker-compose down
```

# Service APIs

* POST http://localhost:5000/users
* GET http://localhost:5000/users/1
* PUT http://localhost:5000/users/1
* DELETE http://localhost:5000/users/1

## POST Example 
POST: http://localhost:5000/users
Content-Type: application/json 

Body:
```
{
  "firstName": "Anderson",
  "lastName": "Silva",
  "email": "anderson@email.com"
}
```

Response:
```
{
    "id": 1,
    "firstName": "Anderson",
    "lastName": "Silva",
    "email": "anderson@email.com",
    "date_created": "2018-06-06T18:23:29",
    "date_updated": null,
    "_links": {
        "self": {
            "href": "http://localhost:5000/users/1"
        }
    }
}
```

# Meta
Distributed under the Unlicense license. See LICENSE for more information.
