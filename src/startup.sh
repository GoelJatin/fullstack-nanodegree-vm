# Setup DB
pipenv run python src/database/database_setup.py

# Load dummy data in DB
pipenv run python src/database/lots_of_menus.py

# Keep the container running

tail -f /dev/null
