# Docker :: Django :: Vue :: PostgreSQL

This is a simple template to create an full-stack application, with:
 - **Backend** in Django (Python)
 - **Frontend** in Vue (Javascript)
 - **Database** in PostgreSQL
 - **Infrastructure** using docker

## Run

```
    docker-compose up --build
```

### This command:
- It will create 3 different containers/images: frontend, backend and database. 
- By default the **Vue** app will be running in http://localhost:8081/. You can change this in the docker-compose file (in the port of the frontend service)
- By default the **Django** app will be running in http://localhost:8000/. You can change this in the docker-compose file (in the port of the backend service)
