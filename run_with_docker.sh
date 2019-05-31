#!/bin/bash
echo "*** Docker Version ***"
docker -v
echo ""
echo ""
echo "*** Docker Build ***"
docker build --iidfile image.id -t api-test:latest .
cat image.id
echo ""
echo ""
echo "*** Test Docker ***"
IMAGE_ID=$(cat image.id)
rm -f image.id
docker run -i -u 1000:1000 -v $PWD:/workspace/ -w /workspace ${IMAGE_ID} python runner.py