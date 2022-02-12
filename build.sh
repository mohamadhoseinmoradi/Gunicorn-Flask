#!/bin/bash
set -e

image_name=$1
image_tag=$2

if [[ $# -lt 2 ]] ; then
    echo "you have to pass at least two arguments!"
    echo "usage: docker-build.sh <image_name>:<image_tag>"
    exit 1
fi

docker build --file Dockerfile --tag  $image_name:$image_tag .
#docker tag app:0.1 artifactory.jfrog.io/app/app:0.1
#docker push artifactory.jfrog.io/app/app:0.1
