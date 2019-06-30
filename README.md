# Convoy
Convoy is a social media project made with Django<br>

## Installation(Docker)
### Static Files
To collect static files for nginx to access, just run:
```bash
$ docker-compose exec web bash
$ python manage.py collectstatic
```
### Migrations
```
docker-compose run web python3 manage.py migrate
```
### Execution
Run docker-compose commands to start containers:
```
$ docker-compose up -d
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
