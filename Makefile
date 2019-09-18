.PHONY: help

DJANGO_CMD = python catalog/manage.py

SETTINGS = config.settings

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Deletes python caches.
	@sudo find . -name "*.pyc" | xargs rm -rf
	@sudo find . -name "*.pyo" | xargs rm -rf
	@sudo find . -name "__pycache__" -type d | xargs rm -rf
	@sudo find . -name ".cache" -type d | xargs rm -rf

setup-env:  ## Copy the sample env file as configuration.
	@mkdir -p logs
	@cp -n contrib/localenv .env

migrations:  ## Create the migrations for python app. e.g. 'make migrations app=core'.
	@mkdir -p logs
	$(DJANGO_CMD) makemigrations $(app)

migrate:  ## Apply the database migrations.
	@mkdir -p logs
	$(DJANGO_CMD) migrate

requirements:  ## Install project requirements through pip.
	@pip install --upgrade pip
	@pip install --no-cache-dir -r requirements/base.txt

requirements-dev:  ## Install project requirements through pip for a development environment.
	@pip install --upgrade pip
	@pip install -r requirements/dev.txt

test: SHELL:=/bin/bash
test: clean  ## Run test suite with debugger support.
	@mkdir -p logs
	py.test catalog --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

singletest: SHELL:=/bin/bash
singletest: clean  ## Run a specific test. e.g. 'make singletest name=test_function_name'
	@mkdir -p logs
	py.test catalog -k $(name) --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

coverage: SHELL:=/bin/bash
coverage: clean  ## Run the coverage reports.
	@mkdir -p logs
	py.test --cov-config .coveragerc --cov catalog catalog --ds=$(SETTINGS) --cov-report term-missing

shell: clean  ## Run a python shell.
	@mkdir -p logs
	$(DJANGO_CMD) shell

runserver: clean setup-env migrate  ## Run the python app (development server).
	@mkdir -p logs
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --noreload

admin-ui-superuser:  ## Create the django admin superuser.
	@mkdir -p logs
	$(DJANGO_CMD) createsuperuser

upload_sample_csv_to_import_api:  ## Upload a sample CSV to import endpoint to populate the database table.
	cd contrib && ./upload_csv_to_api.sh && cd ..

lint: clean  ## Run pylint
	@mkdir -p logs
	@pylint --rcfile=.pylintrc catalog/*

setup: requirements-dev setup-env migrate  ## Setup the environment
	@echo 'Setup finished.'

container:  ## Re(build) the app docker container.
	./rebuild_container.sh

enter-container:  ## Enter (open a bash shell) to the app docker container.
	@echo '=== YOU WILL NOW ENTER catalog DOCKER CONTAINER. HAVE FUN! ==='
	@sudo docker exec -it $$(sudo docker ps | grep catalog | awk '{ print $$1}') /bin/bash
