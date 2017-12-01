############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# use python 3 as base image
FROM python:3

# some environment variables
ENV PYTHONUNBUFFERED 1

# create work directory
WORKDIR /srv

# copy source code
ADD . /srv/

RUN pip install -r requirements.txt

ENTRYPOINT ["/srv/docker-entrypoint.sh"]
