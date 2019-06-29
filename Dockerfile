FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

ADD ./src /code
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations comments
RUN python manage.py makemigrations post
RUN python manage.py makemigrations userprofiles
RUN python manage.py migrate 
