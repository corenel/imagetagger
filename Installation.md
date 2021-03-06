# Installation
## Run on local machine

1. install required python packages.

```
pip3 install -r requirements.txt
```

2. install postgresql

```
# for Ubuntu
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```

3. create database and user (for example, database `imagetagger` and user `imagetagger` with password `imaegtagger`)

```
sudo -u postgres psql
CREATE DATABASE imagetagger;
CREATE USER imagetagger WITH PASSWORD 'imagetagger';
ALTER ROLE imagetagger SET client_encoding TO 'utf8';
ALTER ROLE imagetagger SET default_transaction_isolation TO 'read committed';
ALTER ROLE imagetagger SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE imagetagger TO imagetagger;
```

4. create `imagetagger/imagetagger/settings.python` in template of `imagetagger/imagetagger/settings.py.example`

4. migrate

```
python3 imagetagger/manage.py migrate
```

5. runserver
```
python3 imagetagger/manage.py runserver
```

## Run in Docker
Just build image and run it:

```
# build
docker-compose up --build -d
# run
docker-compose up
```

Then you can look at [http://localhost:8080/](http://localhost:8080/) for imagetagger.

Note that it's necessary to turn on `DJANGO_MANAGEPY_MIGRATE` flag for initialization and migration. Once it's done, you could turn it off.
