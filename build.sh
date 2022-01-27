#!/bin/bash
set -e

image_name=$1
image_tag=$2

if [[ $# -lt 2 ]] ; then
    echo "you have to pass at least two arguments!"
    echo "usage: docker-build.sh <image_name>:<image_tag>"
    exit 1
fi

docker build -f docker/Dockerfile -t  $image_name:$image_tag .