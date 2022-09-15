#!/bin/bash

echo 'Deploy ...'
if [ "$1" = "dev" ]; then
                git pull
		cp mt/mt/settings.dev.py mt/mt/settings.py
		echo 'Development configs has been installed'
elif [ "$1" = "prod" ]; then
				git pull
		cp mt/mt/settings.prod.py mt/mt/settings.py
		echo 'Production configs has been installed'
else
		echo 'Wrong mode'
		exit 1
fi

. venv/bin/activate

pip install -r requirements.txt

if [ ! -d static-static ]; then
	cd mt
	python manage.py collectstatic
fi

sudo service supervisor restart
