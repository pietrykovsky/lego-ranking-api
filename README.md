# lego-scrape-api
API for cataloging and retrieving lego sets by price per element ratio.

## Features
* retrieving lego sets ordered by price per element ratio
* pagination
* flitering, ordering and searching system
* selenium bot scraping data from lego store
* refreshing database with celery task scheduled every 3 hours
* documentation made with drf_spectacular
* customized admin panel

## Requirements
* docker and docker compose

## Installation
Firstly, clone the repository from the github to your local folder with the following command:
```
git clone https://github.com/pietrykovsky/lego-scrape-api.git
```

Next, create an `.env` file where the `docker-compose.yml` is and copy the content from the `.env.sample` file. Example:
```env
DJANGO_SECRET_KEY='your secret key'
DJANGO_ALLOWED_HOSTS=127.0.0.1
DJANGO_DEBUG=True
DJANGO_SETTINGS_MODULE=api.settings

REDIS_CLOUD_URL='redis://redis:6379'

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
```

In the same directory, where the `docker-compose.yml` is, run the following commands:
```
docker compose build
```

## Usage

To start the container and test the api run the following command:
```
docker compose up
```

Now you can head over to http://127.0.0.1:8000/api/docs/ to test the api

To stop the container run:
```
docker compose down
```

To create admin account run:
```
docker compose run --rm api python manage.py createsuperuser
```