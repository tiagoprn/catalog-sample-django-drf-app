- [X] KICKSTART (branch master)
    - [x] Create the django project structure, with a `health_check` app to bootstrap swagger.
    - [x] Create a `core` app, with will contain the product model. Implement the REST Framework
      serializers and REST views.

- [x] MILESTONE 1
    - [x] Rename the "product" model to "pants".
    - [x] Fix issues on `make lint`
    - [x] Create tests for the views.
        - [x] get
        - [x] post

- [x] MILESTONE 2
    - [x] pagination on the pants get (all) view.
    - [x] django-filter on the pants get (all) view.
    - [x] Delete current sqlite database, generate another and 
          re-run the factory to get more sane values to explore the API.   
    - [x] check pagination with the django filter (check with 2 filters)

- [x] MILESTONE 3
    - [x] Enable and configure django-admin.

- [x] MILESTONE 4
    - [x] Create the view to import the CSVs (check import is right with django-admin.)
    - [x] Create tests for the view that imports the CSVs.

- [x] MILESTONE 5
    - [x] Finish tests for the views.
        - [x] put
        - [x] patch
        - [x] delete
        - [x] get with pagination and filters

- [ ] MILESTONE FINAL
    - [x] See why the choicefields on factory are not persisting just the value, but the whole tuple.
    - [x] Include on the Makefile a command to trigger `contrib/upload_csv_to_api.sh`
    - [x] Configure a better logging 
    - [x] Run the linter
    - [x] Create a README.md (explain requirements: ubuntu 18.04, docker, docker-compose to raise
      the image)
    - [x] Create a `make setup` on the Makefile, where it is composed by: 
        `make requirements-dev, make setup-env, make migrate, upload_sample_csv_to_import_api`
    - [x] Create a Docker container from ubuntu 18.04 image (just run Makefile commands on the
      Dockerfile - the skeleton is here at tmp/)
    - [x] Create a docker-compose to run the app image (catalog)
    - [x] Create a Makefile command to run the building from the container from previous step
    - [ ] Create a Makefile command to enter the container (`make container-enter`)
    - [x] Update README.md with instructions to run locally from the makefile.
    - [ ] Add postgres and dj-database-url (will have just 2 envs for now: `dev` and `test`)
    - [ ] Update the docker-compose to run alongside postgres
