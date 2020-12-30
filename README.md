Prueba de desarrollo Backend - Quick
============================================

Prueba para el cargo de Desarrollador backend Quick.

# Instalacion del proyecto
***************************************
.. code-block:: rst

    $ docker-compose up -d
    $ docker exec -it api_quick bash
    $ cd /code
    $ python manage.py migrate
    $ python manage.py createsuperuser


Hecho con ♥ por `Duvan Botello`
***************************************

# Documentacion

# api_quick

----------------

# Introduction
What does your API do?

# Overview
Things that the developers should know about

# Authentication
What is the preferred way of using the API?

# Error Codes
What errors and status codes can a user expect?

# Rate limit
Is there a limit to the number of requests an user can send?

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
> |Key|Value|Description|
> |---|---|---|
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
> > > |Key|Value|Description|
> > > |---|---|---|
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
> > > |Key|Value|Description|
> > > |---|---|---|
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
> > > |Key|Value|Description|
> > > |---|---|---|
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

## /api/users/create

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
> |Authorization|Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ||
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
> **Example: /api/users/create**
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
> **Example: /api/users/create**
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
> **Example: /api/users/create**
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
> **Example: /api/users/create**
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
> > >     "email": "nuevo@example.com",
> > >     "password": "SECRET",
> > >     "age": 42,
> > >     "token": "prueba",
> > >     "image": "IMAGE"
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
> > >   "id": 5,
> > >   "first_name": "John",
> > >   "last_name": "Doe",
> > >   "email": "nuevo@example.com",
> > >   "token": "prueba",
> > >   "age": 42,
> > >   "image": "IMAGE",
> > >   "description": ""
> > > }
> > > ```
> > > 
> > 
> 

----------------

## /api/users/edit/{id}

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
> **Example: /api/users/edit/6**
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

## /api/users/editp/{id}

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
> **Example: /api/users/editp/7**
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

## /api/users/

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
> > > [
> > >   {
> > >     "id": 2,
> > >     "first_name": "Duvan",
> > >     "last_name": "Botello",
> > >     "email": "admin@ggmail.com",
> > >     "token": "inicial",
> > >     "age": 24,
> > >     "image": null,
> > >     "description": ""
> > >   },
> > >   {
> > >     "id": 4,
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "user@example.com",
> > >     "token": "null",
> > >     "age": 42,
> > >     "image": "IMAGE",
> > >     "description": ""
> > >   },
> > >   {
> > >     "id": 5,
> > >     "first_name": "John",
> > >     "last_name": "Doe",
> > >     "email": "nuevo@example.com",
> > >     "token": "prueba",
> > >     "age": 42,
> > >     "image": "IMAGE",
> > >     "description": ""
> > >   },
> > >   {
> > >     "id": 3,
> > >     "first_name": "Duvan",
> > >     "last_name": "Botello",
> > >     "email": "admin@gmail.com",
> > >     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5MzgyMDcyLCJqdGkiOiIxOTI5MWU2MWJlMTU0OWZiYmI5NDI2MmRjZWMyM2FkZCIsInVzZXJfaWQiOjN9.BG1CmkM8IFkuQXY2hzzLMtTds-UlcJE3QjkvBVc69DQ",
> > >     "age": 24,
> > >     "image": null,
> > >     "description": ""
> > >   },
> > >   {
> > >     "id": 6,
> > >     "first_name": "nuevo",
> > >     "last_name": "nuevo",
> > >     "email": "ds@example.com",
> > >     "token": "dsddsd",
> > >     "age": 55,
> > >     "image": null,
> > >     "description": ""
> > >   }
> > > ]
> > > ```
> > > 
> > 
> 

----------------

## /api/users/{id}

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
> **Example: /api/users/2**
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

## /api/users/delete/{id}

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
> **Example: /api/users/delete/7**
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

## /{anything}

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

## /auth/token/

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

Built with [Postdown][PyPI].

Author: [Titor](https://github.com/TitorX)

[PyPI]:    https://pypi.python.org/pypi/Postdown
