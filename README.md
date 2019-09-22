<a href="https://github.com/furkanonder/Convoy/blob/master/LICENSE.txt" target="_blank">
  <img alt="MIT License" title="MIT License" src="https://img.shields.io/github/license/coogger/coogger.svg?style=for-the-badge"/>
</a>

<a href="https://github.com/psf/black" target="_blank">
 <img alt="Code style" title="Code style" src="https://img.shields.io/badge/Code%20style-black-black?style=for-the-badge"/>
</a>

<a href="https://github.com/timothycrosley/isort" target="_blank">
  <img alt="Code style" title="Code style" src="https://img.shields.io/badge/code%20style-isort-lightgrey?style=for-the-badge"/>
</a>

# Convoy
Convoy is a social media project made with Django

## Installation
Clone the repository
```
git clone https://github.com/furkanonder/pasteRand
```
Install the requirements:
```python
pip install -r requirements.txt
```
Make migrations
```python
python manage.py migrate
```
Finally, run the project
```python
python manage.py runserver
```

## Docker
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
