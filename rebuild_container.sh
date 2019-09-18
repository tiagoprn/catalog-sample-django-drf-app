#/bin/bash
sudo docker-compose stop && sudo docker-compose rm -f && sudo docker rmi tiagoprn/catalog; \
    sudo docker-compose build --no-cache --build-arg UID=$(id -u) --build-arg GID=$(id -g) catalog && sudo docker-compose up -d
