# Simple REST-API Flask

This repo contains the simplest example of a REST-API with flask.

The purpose of this application is to be part of a microservices ecosystem and communicate with them through RabbitMQ.

## Endpoints
The API only have a `User` resource, and the endpoints that are allowed are

### Create

`POST /users/`

```json
{
  "user_name": "juan23",
  "password": "myP4ssword",
  "name": "Juan Perez"
}
```

### Retrieve

`GET /users/{user_id}/`
```json
{
  "identifier": 3,
  "user_name": "juan23",
  "name": "Juan Perez"
}
```

## TODO
* Encode the password.
