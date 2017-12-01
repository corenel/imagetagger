#!/bin/sh
set -e

# until psql $DATABASE_URL -c '\l'; do
#   >&2 echo "Postgres is unavailable - sleeping"
#   sleep 1
# done

# >&2 echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python /srv/imagetagger/manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    python /srv/imagetagger/manage.py collectstatic --noinput
fi

if [ "x$DJANGO_MANAGEPY_DUMPDATA" = 'xon' ]; then
    python /srv/imagetagger/manage.py \
        dumpdata --format=json annotations \
        > /srv/imagetagger/imagetagger/annotations/fixtures/initial_data.json
elif [ "x$DJANGO_MANAGEPY_LOADDATA" = 'xon' ]; then
    python /srv/imagetagger/manage.py loaddata --app annotations
fi

exec "$@"
