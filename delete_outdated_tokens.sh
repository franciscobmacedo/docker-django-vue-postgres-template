#!/bin/sh

docker exec -it backend
python manage.py shell < delete_outdated_tokens.py