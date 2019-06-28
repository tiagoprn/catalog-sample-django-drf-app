# catalog

This project exposes a browsable CRUD REST API that can be used on a store's pants' catalog.
You can also mass import pants' records on the API through a CSV file, and browse and
search through the catalog through an admin interface for convenience.

# Technologies

- Python 3.7
- Django and Django REST Framework
- Swagger
- pytest
- docker / docker-compose

# Development environment

This project was developed on Arch Linux, using `pyenv` and `pyenv-virtualenv`, with PyCharm as the
IDE.

# Installation

## Requirements

Since the solution is dockerized, the only requirements are `docker` and `docker-compose`. So any
linux distro (including Ubuntu 18.04) is supported.

## How to run locally

First, create a virtualenv, using the tooling at your disposal.  

A Makefile is available to automate the full setup process (and other development jobs also ;).

- To setup the environment: 

`make setup`

- To raise the local development server: 

`make runserver`

- To create an admin user to browse the catalog records locally: 

`make admin_ui_superuser`

## After finished

A browsable REST API is available through swagger at http://localhost:8000.

An admin interface where you can browse and search through all data is available at
http://localhost:8000/admin.

IMPORTANT: To upload a CSV to the API, you cannot use swagger. So, it was provided a shell script
that runs curl at `contrib/upload_csv_to_api.sh` that you can use as an example on how to do that.

