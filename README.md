# Convoy
Convoy is a social media project made with Django<br>

## Installation(Docker)
Run docker-compose commands to start containers
```
docker-compose up -d
```
Get the container id.
```
docker ps -aqf "name=convoy_web" 
```
Access the terminal with this id.
```
docker exec -it <id> /bin/bash
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
