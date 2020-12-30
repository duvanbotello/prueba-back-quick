Prueba de desarrollo Backend - Quick
============================================

Prueba para el cargo de Desarrollador backend Quick.

## Software Usado
 * Python (Django Rest Framework)
 * Git
 * GitHub
 * PostgreSQL
 * Docker
 * Simple JWT (Django Rest Framework)
 * AWS EC2
 * Documentacion Markdown
 * Postman

## Instalacion del proyecto
***************************************

    $ docker-compose up -d
    $ docker exec -it api_quick bash
    $ python manage.py migrate
    $ python manage.py createsuperuser


Hecho con ♥ por `Duvan Botello`
***************************************

# Documentacion
____________________

## Autenticación
**JWT simple**

Simple JWT proporciona un backend de autenticación JSON Web Token para Django REST Framework. Su objetivo es cubrir los casos de uso más comunes de JWT ofreciendo un conjunto conservador de características predeterminadas. También pretende ser fácilmente extensible en caso de que no esté presente una característica deseada.

**¿Como Autenticarme?**

La API REST posee un Endpoints que permite iniciar session en el sistema y nos suministra el token de autorizacion necesario. El token que nos genere se debe colocar como cabezara para acceder a los Endpoints portegidos.

Cada peticion debe tener la siguente estructura en su Header.

> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzQ5NTkyLCJqdGkiOiJjYTU3ZDU5YjhkZmU0NjBjYWY5M2IzYTU5Mjc4YTIyMCIsInVzZXJfaWQiOjF9.QaVKdFFcbXcUqKvO5xSbRCq6tlAOv8F3UvzCxTbsRPU||
> > > 

----------------

## /api/login

```
POST http://3.129.92.204:8000/api/login
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|
> |---|---|
> |Content-Type|application/json||
> 
> **Body**
> 
> ```
> {
> 	"email": "admin@gmail.com", 
> 	"password": "admin456123"
> 	
> }
> ```
> 

### Examples:

> 
> **Example: /api/login**
> 
> > 
> > ```
> > POST http://3.129.92.204:8000/api/login
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |---|---|
> > > |Content-Type|application/json||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > > 	"email": "admin@gmail.com", 
> > > 	"password": "admin456123"
> > > 	
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 3,
> > >   "first_name": "Duvan",
> > >   "last_name": "Botello",
> > >   "email": "admin@gmail.com",
> > >   "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5Mzc2NDUzLCJqdGkiOiIxNzkxOWM5N2I1OGE0YWU5Yjc3Y2I2NWJiNDk4YzBjNCIsInVzZXJfaWQiOjN9.AxsjDJmHzzDGXuPDyAXt1gHtPJFP2YKl6OwrD0P7QQ0",
> > >   "age": 24,
> > >   "image": null,
> > >   "description": ""
> > > }
> > > ```
> > > 
> > 
> 
> **Example: /api/login**
> 
> > 
> > ```
> > POST http://3.129.92.204:8000/api/login
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |---|---|
> > > |Content-Type|application/json||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > > 	"email": "admin@gmail.com", 
> > > 	"password": ""
> > > 	
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "error": "Error in user or password"
> > > }
> > > ```
> > > 
> > 
> 


----------------
# Endpoints
----------------

## POST /api/users/create "Realizar un nuevo registro"

```
POST http://3.129.92.204:8000/api/users/create
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer TOKEN JWT||
> 
> **Body**
> 
> ```
> {
>     "first_name": "nuevo",
>     "last_name": "nuevo",
>     "email": "ds@example.com",
>     "password": "nueva",
>     "age": 55,
>     "token": "dsddsd"
> }
> ```
> 

### Examples:

> 
> **Example: /api/users/create "Cuando el usuario inicio session, pero no actualizo el token jwt en el Header"**
> 
> > 
> > ```
> > POST http://3.129.92.204:8000/api/users/create
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzQ5NTkyLCJqdGkiOiJjYTU3ZDU5YjhkZmU0NjBjYWY5M2IzYTU5Mjc4YTIyMCIsInVzZXJfaWQiOjF9.QaVKdFFcbXcUqKvO5xSbRCq6tlAOv8F3UvzCxTbsRPU||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >     "first_name": "nuevo",
> > >     "last_name": "nuevo",
> > >     "email": "ds@example.com",
> > >     "password": "nueva",
> > >     "age": 155,
> > >     "token": "dsddsd"
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "detail": "User not found",
> > >   "code": "user_not_found"
> > > }
> > > ```
> > > 
> > 
> 
> **Example: /api/users/create "Cuando ejecuta la peticion de manera correcta"**** 
> 
> > 
> > ```
> > POST http://3.129.92.204:8000/api/users/create
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5Mzc3MDUyLCJqdGkiOiJmNDc2ZmNkY2M2ZGI0OTM5OTQ1OWJmNTIxMzI1NzRjYSIsInVzZXJfaWQiOjN9.VluB1OQVKbN0mVkvdNPqaoQJfVhJ6jtl0WH0Tcw3jwk||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "user@example.com",
> > >     "password": "SECRET",
> > >     "age": 42,
> > >     "image": "IMAGE",
> > >     "token": "null"
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 4,
> > >   "first_name": "John",
> > >   "last_name": "Doe",
> > >   "email": "user@example.com",
> > >   "token": "null",
> > >   "age": 42,
> > >   "image": "IMAGE",
> > >   "description": ""
> > > }
> > > ```
> > > 
> > 
> 
> **Example: /api/users/create "Cuando el cuerpo de la peticion va vacio"**
> 
> > 
> > ```
> > POST http://3.129.92.204:8000/api/users/create
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5Mzc3MDUyLCJqdGkiOiJmNDc2ZmNkY2M2ZGI0OTM5OTQ1OWJmNTIxMzI1NzRjYSIsInVzZXJfaWQiOjN9.VluB1OQVKbN0mVkvdNPqaoQJfVhJ6jtl0WH0Tcw3jwk||
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "message": "empty body"
> > > }
> > > ```
> > > 
> > 
> 

----------------

## PUT /api/users/edit/{id} "Actualizar los datos de un registro en especifico"

```
PUT http://3.129.92.204:8000/api/users/edit/2
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> 
> **Body**
> 
> ```
> {
>     "first_name": "John",
>     "last_name": "Doe",
>     "email": "user@example.com",
>     "password": "SECRET",
>     "age": 24,
>     "image": "IMAGE",
>     "description": "Description text",
>     "token": "dsdsd"
> }
> ```
> 

### Examples:

> 
> **Example: /api/users/edit/6 "Mejor de los casos"**
> 
> > 
> > ```
> > PUT http://3.129.92.204:8000/api/users/edit/2
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "nuevor@example.com",
> > >     "password": "SECRET",
> > >     "age": 24,
> > >     "image": "IMAGE",
> > >     "description": "Description text",
> > >     "token": "nuevo"
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 2,
> > >   "first_name": "John",
> > >   "last_name": "Doe",
> > >   "email": "nuevor@example.com",
> > >   "token": "nuevo",
> > >   "age": 24,
> > >   "image": "IMAGE",
> > >   "description": "Description text"
> > > }
> > > ```
> > > 
> > 
> 

----------------

## PATCH /api/users/editp/{id} "Actualizar datos parciales de un reigstro"

```
PATCH http://3.129.92.204:8000/api/users/editp/2
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> 
> **Body**
> 
> ```
> {
>     "first_name": "modificado",
>     "last_name": "modifcado",
>     "age": 105,
>     "description": "nuevo texto"
> }
> ```
> 

### Examples:

> 
> **Example: /api/users/editp/7 "Mejor de los casos"**
> 
> > 
> > ```
> > PATCH http://3.129.92.204:8000/api/users/editp/2
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >     "first_name": "Steven",
> > >     "last_name": "Smith",
> > >     "age": 26
> > > }
> > > ```
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 2,
> > >   "first_name": "Steven",
> > >   "last_name": "Smith",
> > >   "email": "nuevor@example.com",
> > >   "token": "nuevo",
> > >   "age": 26,
> > >   "image": "IMAGE",
> > >   "description": "Description text"
> > > }
> > > ```
> > > 
> > 
> 

----------------

## GET /api/users/ "Lista todos los usuarios"

```
GET http://3.129.92.204:8000/api/users/
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> 

### Examples:

> 
> **Example: /api/users/**
> 
> > 
> > ```
> > GET http://3.129.92.204:8000/api/users/
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5Mzc3MDUyLCJqdGkiOiJmNDc2ZmNkY2M2ZGI0OTM5OTQ1OWJmNTIxMzI1NzRjYSIsInVzZXJfaWQiOjN9.VluB1OQVKbN0mVkvdNPqaoQJfVhJ6jtl0WH0Tcw3jwk||
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > [
> > >   {
> > >     "id": 2,
> > >     "password": "pbkdf2_sha256$216000$87mYTtRaH1kQ$mErYVL5EZHGiOfmIr93DVAGFzehIkw5GMsKKdV1nejw=",
> > >     "last_login": null,
> > >     "first_name": "Duvan",
> > >     "last_name": "Botello",
> > >     "email": "admin@ggmail.com",
> > >     "token": "inicial",
> > >     "age": 24,
> > >     "image": null,
> > >     "description": "",
> > >     "is_active": true,
> > >     "is_admin": true
> > >   },
> > >   {
> > >     "id": 4,
> > >     "password": "pbkdf2_sha256$216000$8SAmtkD8fMDd$cCgPEcR6xYzEcIhHntVEu2WWwyCnuAmuSFgFHvoZKtU=",
> > >     "last_login": null,
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "user@example.com",
> > >     "token": "null",
> > >     "age": 42,
> > >     "image": "IMAGE",
> > >     "description": "",
> > >     "is_active": true,
> > >     "is_admin": false
> > >   },
> > >   {
> > >     "id": 3,
> > >     "password": "pbkdf2_sha256$216000$IEv8dWdqDIRb$xSZg/B26Sq4Z1wb7v3YWmgjzVtvxP74iGCBixFU+UDA=",
> > >     "last_login": null,
> > >     "first_name": "Duvan",
> > >     "last_name": "Botello",
> > >     "email": "admin@gmail.com",
> > >     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5Mzc5OTg0LCJqdGkiOiJlMWVlZjcyZTcwOGI0MDExOGE2OTUxZDVhZjQyMDUwYiIsInVzZXJfaWQiOjN9.RB_p7sv2TCP3RJFpvwlJ-LTvDpgp2WDWZAlQCUbkOBk",
> > >     "age": 24,
> > >     "image": null,
> > >     "description": "",
> > >     "is_active": true,
> > >     "is_admin": true
> > >   },
> > >   {
> > >     "id": 5,
> > >     "password": "pbkdf2_sha256$216000$aB4KWaeiOlqA$YApFuOacriEYLZbeRhl0I2kCdsiG6UJEM/Z4UiHxGuc=",
> > >     "last_login": null,
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "nuevo@example.com",
> > >     "token": "prueba",
> > >     "age": 42,
> > >     "image": "IMAGE",
> > >     "description": "",
> > >     "is_active": true,
> > >     "is_admin": false
> > >   }
> > > ]
> > > ```
> > > 
> > 
> 

----------------

## GET /api/users/{id} "Listar un usuario en especifico"

```
GET http://3.129.92.204:8000/api/users/2
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> 

### Examples:

> 
> **Example: /api/users/2 "Mejor de los casos"**
> 
> > 
> > ```
> > GET http://3.129.92.204:8000/api/users/3
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 3,
> > >   "first_name": "Duvan",
> > >   "last_name": "Botello",
> > >   "email": "admin@gmail.com",
> > >   "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ",
> > >   "age": 24,
> > >   "image": null,
> > >   "description": ""
> > > }
> > > ```
> > > 
> > 
> 

----------------

## DELETE /api/users/delete/{id} "Eliminar un registro de la base de datos"

```
DELETE http://3.129.92.204:8000/api/users/delete/4
```



----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> 

### Examples:

> 
> **Example: /api/users/delete/7  "Mejor de los casos"**
> 
> > 
> > ```
> > DELETE http://3.129.92.204:8000/api/users/delete/4
> > ```
> > 
> > **Request**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |---|---|---|
> > > |Content-Type|application/json||
> > > |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "id": 4,
> > >   "first_name": "John",
> > >   "last_name": "Doe",
> > >   "email": "user@example.com",
> > >   "token": "null",
> > >   "age": 42,
> > >   "image": "IMAGE",
> > >   "description": ""
> > > }
> > > ```
> > > 
> > 
> 

----------------

## GET /{anything} "Cuando se ingresa una ruta que no existe dentro de la API"

```
GET http://3.129.92.204:8000/cualquiercosa
```



----------------

### Request

> 

### Examples:

> 
> **Example: /{anything}**
> 
> > 
> > ```
> > GET http://3.129.92.204:8000/cualquiercosa
> > ```
> > 
> > **Request**
> > 
> > > 
> > 
> > ----------------
> > 
> > **Response**
> > 
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "error": "Not found"
> > > }
> > > ```
> > > 
> > 
> 

----------------

## POST /auth/token/ "Para generar un nuevo token"

```
POST http://18.223.124.251:8000/auth/token/
```

Endpoints para generar JSON Web Token

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzQ5NTkyLCJqdGkiOiJjYTU3ZDU5YjhkZmU0NjBjYWY5M2IzYTU5Mjc4YTIyMCIsInVzZXJfaWQiOjF9.QaVKdFFcbXcUqKvO5xSbRCq6tlAOv8F3UvzCxTbsRPU||
> 
> **Body**
> 
> ```
> {
> 	"email": "admin@gmail.com", 
> 	"password": "admin"
> 	
> }
> ```
> 

### Examples:

> 

----------------

----------------
