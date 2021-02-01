# Docker :: Django :: Vue :: PostgreSQL

This is a simple template to create a full-stack application with:
 - **Backend** in Django (Python)
 - **Frontend** in Vue (Javascript)
 - **Database** in PostgreSQL
 - **Infrastructure** using docker

## Run

In the main folder, run:
```
    docker-compose up --build
```


- It will create 3 different containers/images: frontend, backend and database. 
- By default the **Vue** app will be running in http://localhost:8081/. You can change this in the docker-compose file (in the port of the frontend service)
- By default the **Django** app will be running in http://localhost:8000/. You can change this in the docker-compose file (in the port of the backend service)


## Master Branch
In the master branch, its a simple application with connections between django and vue.

## auth Branch
In auth branch, there's a built-in authentication system, using djangorestframework and JWT authentication.
