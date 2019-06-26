- [ ] MILESTONE 1
    - [ ] Rename the "product" model to "pants".
    - [ ] Create tests for the serializers and views.
    - [ ] Create a README.md (explain requirements: ubuntu 18.04, docker, docker-compose to raise
      the image)


- [ ] MILESTONE FINAL
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
