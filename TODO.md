- [ ] MILESTONE 1
    - [x] Rename the "product" model to "pants".
    - [x] Fix issues on `make lint`
    - [ ] Create tests for the serializers and views.


- [ ] MILESTONE 2
    - [ ] Enable and configure django-admin.

- [ ] MILESTONE 3
    - [ ] Create the view to import the CSVs (check import is right with django-admin.)

- [ ] MILESTONE FINAL
    - [ ] Create a README.md (explain requirements: ubuntu 18.04, docker, docker-compose to raise
      the image)
    - [ ] Extract the lists used to validate the ChoiceFields to constant classes.
    - [ ] Create a Docker container from ubuntu 18.04 image (just run Makefile commands on the
      Dockerfile)
    - [ ] Create a Makefile command to run the building from the container from previous step, push
      to dockerhub
    - [ ] Add postgres and dj-database-url
    - [ ] Create a docker-compose to run the app image (catalog) and postgresql, using my previous
      postgres templates.
    - [ ] Update README.md with instructions to run locally from the docker-compose image.

- [X] KICKSTART (branch master)
    - [x] Create the django project structure, with a `health_check` app to bootstrap swagger.
    - [x] Create a `core` app, with will contain the product model. Implement the REST Framework
      serializers and REST views.
