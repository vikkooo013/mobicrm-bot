# /bin/bash
python -m rasa run actions --actions actions -p 5055 --debug >> logs/rasa_action-`/bin/date +\%Y-\%m-\%d-\%H-\%M-\%S`.log &
python -m rasa run -m models --endpoints endpoints.yml -p 5002 --enable-api --credentials credentials.yml --log-file logs/rasa_core-`/bin/date +\%Y-\%m-\%d-\%H-\%M-\%H-\%M-\%S`.log --debug