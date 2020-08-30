#!/usr/bin/env bash
#build image
docker build --tag=api .

#list images
docker image ls

#run api image by mapping port 5001 to 8000
docker run -p 8000:5001 api