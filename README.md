# MyMDB 
> from the book Building Django Web Applications 

MyMDB has two types of users: users and administrators. The users will be able to rate movies, add images from movies, and view movies and cast. The administrators will be able to add movies, actors, writers, and directors.


## Installation

Install [Docker Compose](https://docs.docker.com/compose/install/)

List the variables in `.env` file.

```
# Django settings
DJANGO_SETTINGS_MODULE=config.production_settings
DJANGO_SECRET_KEY=#put your secret key here
DJANGO_LOG_LEVEL=DEBUG
DJANGO_LOG_FILE=/var/log/mymdb/mymdb.log
DJANGO_ALLOWED_HOSTS=# put your domain here
DJANGO_DB_NAME=mymdb
DJANGO_DB_USER=mymdb
DJANGO_DB_PASSWORD=#put your password here
DJANGO_DB_HOST=db
DJANGO_DB_PORT=5432
DJANGO_CACHE_TIMEOUT=200

AWS_ACCESS_KEY_ID=# put aws key here
AWS_SECRET_ACCESS_KEY_ID=# put your secret key here
DJANGO_UPLOAD_S3_BUCKET=# put BUCKET_NAME here

# Postgres settings
POSTGRES_PASSWORD=# put your postgress admin password here
```

To start containers locally, run the following command:

```sh
docker-compose up -d
```
