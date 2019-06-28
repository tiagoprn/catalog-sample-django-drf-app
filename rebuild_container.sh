#!/bin/bash
sudo docker-compose stop && sudo docker-compose rm -f && sudo docker rmi tiagoprn/catalog; \
    sudo docker-compose build --no-cache && sudo docker-compose up -d && sudo docker-compose logs -f;
