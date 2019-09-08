# Convoy
Convoy is a social media project made with Django

## Installation(Docker)
Run docker-compose commands to start containers
```
docker-compose up -d
```
Log in to the terminal.
```
docker exec -it convoy_web_1 /bin/bash
```
Make migrations.
```
python manage.py migrate --noinput
```
And finally, collect static files.
```
python manage.py collectstatic
```
## Features
* CRUD operations for posts.
* Search for users and titles.
* Users can edit their profile(name,surname,email and password)
* Rest-Api (you can get the post contents)
* Comment replay    
## To do list
* Topic
* Captcha verification
* User follow system
