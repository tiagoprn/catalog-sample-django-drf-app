# catalog

This project exposes a browsable CRUD REST API that can be used on a store's pants' catalog.
You can also mass import pants' records on the API through a CSV file, and browse and
search through the catalog through an admin interface for convenience.

Almost all the API is covered with successful-failure automated tests scenarios. 
Just the csv import one was covered on the business module - so all the 
critical decision branches are covered there. 

# Technologies

- Python 3.7
- Django and Django REST Framework
- Swagger
- pytest
- SQLite (*)
- docker / docker-compose

(*) Given the focus I got on the API working with full test coverage, I had left to change
to Postgres at a later time, since I prefer it as a relational database. But to deliver on time, 
I had left that idea.  

# Development environment

This project was developed on Arch Linux, using `pyenv` and `pyenv-virtualenv`, with PyCharm as the
IDE.

# Installation

## Requirements

Since I recomend to **install on docker** so not to clutter your environment, 
the only requirements are **`docker` and `docker-compose`**. So any
linux distro (including Ubuntu 18.04) is supported, since docker is 
os-independent.

### OPTION 1 - Run locally through **docker**

This will build a docker container ready to be used: 

`make container`

Then, to execute other operations, enter the container: 

`make enter-container`

To create an admin user to browse the catalog records locally:

`make admin-ui-superuser`

- To run the test suite: 

`make test`

- To run the tests coverage report: 

`make coverage`
apt
Now, go to the section "After finished" below on this file to check 
what you can do.

### OPTION 2 - Run locally with a **virtualenv**

First, **create a virtualenv** based on `python 3.5+` , using the tooling at your disposal.  

A Makefile is available to automate the full setup process (and other development jobs also ;).

- To setup the environment: 

`make setup`

- To raise the local development server: 

`make runserver`

- To create an admin user to browse the catalog records locally: 

`make admin-ui-superuser`

- To run the test suite: 

`make test`

- To run the tests coverage report: 

`make coverage`

Now, go to the section "After finished" below on this file to check 
what you can do.


## After finished

A browsable REST API is available through swagger at http://localhost:8000.

An admin interface where you can browse and search through all data is available at
http://localhost:8000/admin.

IMPORTANT: To upload a CSV to the API, you cannot use swagger. So, it was provided a shell script
that runs curl at `contrib/upload_csv_to_api.sh` that you can use as an example on how to do that.
If for convenience you want to run the provided one, you can run `make upload_sample_csv_to_import_api`.
You can use the admin interface mentioned before to confirm the CSV data was successfully uploaded.
