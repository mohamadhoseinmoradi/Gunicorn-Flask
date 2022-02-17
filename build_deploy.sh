#!/bin/bash
set -e

image_name=$1
image_tag=$2
release_name=$3

if [[ $# -lt 3 ]] ; then
    echo "you have to pass at least three arguments!"
    echo "usage: docker-build.sh <image_name> <image_tag> <release_name>"
    exit 1
fi

echo "building the artifact ..."
docker build --file Dockerfile --tag  $image_name:$image_tag .
echo "Done"

echo "running pytest ..."
pytest -v
echo "Done"

echo "tagging and pushing the artifact ..."
docker tag $image_name:$image_tag mdmddockergft/$image_name:$image_tag
docker push mdmddockergft/$image_name:$image_tag
echo "Done"

echo "deploying application - running Helm ..."
helm install $release_name helm/
echo "Done"
