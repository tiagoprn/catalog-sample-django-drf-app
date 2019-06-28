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
	@echo -e " make requirements-apt \n\t Install packages on the distribution to support installation through pip.\n"
	@echo -e " make check-debugger \n\t Find ipdb references.\n"
	@echo -e " make test-ci \n\t Run test suite.\n"
	@echo -e " make test \n\t Run test suite with debugger support.\n"
	@echo -e " make singletest \n\t Run a specific test. e.g. 'make singletest name=test_function_name' \n"
	@echo -e " make coverage \n\t Run the coverage reports.\n"
	@echo -e " make shell \n\t Run a python shell.\n"
	@echo -e " make runserver \n\t Run the python app (development server).\n"
	@echo -e " make admin_ui_superuser \n\t Create the django admin superuser.\n"
	@echo -e " make upload_sample_csv_to_import_api \n\t Upload a sample CSV to import endpoint to populate the database table.\n"
	@echo -e " make lint \n\t Run pylint.\n"

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf

setup-env:
	@cp -n contrib/localenv .env

migrations:
	$(DJANGO_CMD) makemigrations $(app)

migrate:
	$(DJANGO_CMD) migrate

requirements:
	@pip install --upgrade pip
	@pip install -r requirements/base.txt

requirements-dev:
	@pip install --upgrade pip
	@pip install -r requirements/dev.txt

requirements-apt:
	@echo 'Root access required to install system dependencies from `requirements.apt` file'
	@sudo apt-get install $(shell cat requirements.apt | tr "\n" " ")

check-debugger:
	@find catalog -type f -exec egrep -iH "set_trace" {} \+ && echo "Ooops! Found 1 set_trace on your source code!" && exit 1 || exit 0

test-ci: SHELL:=/bin/bash
test-ci: clean
	py.test -vvv catalog --ds=$(SETTINGS)

test: SHELL:=/bin/bash
test: clean
	py.test catalog --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

singletest: SHELL:=/bin/bash
singletest: clean
	py.test catalog -k $(name) --ds=$(SETTINGS) -s -vvv --pdbcls=IPython.core.debugger:Pdb

coverage: SHELL:=/bin/bash
coverage: clean
	py.test --cov-config .coveragerc --cov catalog catalog --ds=$(SETTINGS) --cov-report term-missing

shell: clean
	$(DJANGO_CMD) shell

runserver: clean
	mkdir -p log && $(DJANGO_CMD) runserver 0.0.0.0:8000 --noreload

admin_ui_superuser:
	$(DJANGO_CMD) createsuperuser

upload_sample_csv_to_import_api:
	cd contrib && ./upload_csv_to_api.sh && cd ..

lint:
	@pylint -r y --rcfile=.pylintrc catalog/*

