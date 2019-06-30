DJANGO_CMD = python catalog/manage.py

SETTINGS = config.settings

help:
	@echo -e "\nHELP:\n"
	@echo -e " make clean \n\t Deletes python caches.\n"
	@echo -e " make setup-env \n\t Copy the sample env file as configuration.\n"
	@echo -e " make migrations \n\t Create the migrations for python app. e.g. 'make migrations app=core'.\n"
	@echo -e " make migrate \n\t Apply the database migrations.\n"
	@echo -e " make requirements \n\t Install project requirements through pip.\n"
	@echo -e " make requirements-dev \n\t Install project requirements through pip for a development environment.\n"
	@echo -e " make test \n\t Run test suite with debugger support.\n"
	@echo -e " make singletest \n\t Run a specific test. e.g. 'make singletest name=test_function_name' \n"
	@echo -e " make coverage \n\t Run the coverage reports.\n"
	@echo -e " make shell \n\t Run a python shell.\n"
	@echo -e " make runserver \n\t Run the python app (development server).\n"
	@echo -e " make admin-ui-superuser \n\t Create the django admin superuser.\n"
	@echo -e " make upload_sample_csv_to_import_api \n\t Upload a sample CSV to import endpoint to populate the database table.\n"
	@echo -e " make lint \n\t Run pylint.\n"
	@echo -e " make setup \n\t Setup the environment.\n"
	@echo -e " make container \n\t Re(build) the app docker container.\n"
	@echo -e " make enter_container \n\t Enter (open a bash shell) to the app docker container.\n"

clean:
	@sudo find . -name "*.pyc" | xargs rm -rf
	@sudo find . -name "*.pyo" | xargs rm -rf
	@sudo find . -name "__pycache__" -type d | xargs rm -rf
	@sudo find . -name ".cache" -type d | xargs rm -rf

setup-env:
	@mkdir -p logs
	@cp -n contrib/localenv .env

migrations:
	@mkdir -p logs
	$(DJANGO_CMD) makemigrations $(app)

migrate:
	@mkdir -p logs
	$(DJANGO_CMD) migrate

requirements:
	@pip install --upgrade pip
	@pip install --no-cache-dir -r requirements/base.txt

requirements-dev:
	@pip install --upgrade pip
	@pip install -r requirements/dev.txt

test: SHELL:=/bin/bash
test: clean
	@mkdir -p logs
	py.test catalog --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

singletest: SHELL:=/bin/bash
singletest: clean
	@mkdir -p logs
	py.test catalog -k $(name) --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

coverage: SHELL:=/bin/bash
coverage: clean
	@mkdir -p logs
	py.test --cov-config .coveragerc --cov catalog catalog --ds=$(SETTINGS) --cov-report term-missing

shell: clean
	@mkdir -p logs
	$(DJANGO_CMD) shell

runserver: clean setup-env
	@mkdir -p logs
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --noreload

admin-ui-superuser:
	@mkdir -p logs
	$(DJANGO_CMD) createsuperuser

upload_sample_csv_to_import_api:
	cd contrib && ./upload_csv_to_api.sh && cd ..

lint: clean
	@mkdir -p logs
	@pylint -r y --rcfile=.pylintrc catalog/*

setup: requirements-dev setup-env migrate
	@echo 'Setup finished.'

container:
	./rebuild_container.sh

enter-container:
	@echo '=== YOU WILL NOW ENTER catalog DOCKER CONTAINER. HAVE FUN! ==='
	@sudo docker exec -it $$(sudo docker ps | grep catalog | awk '{ print $$1}') /bin/bash
