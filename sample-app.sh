#!/bin/bash

mkdir -p tempdir

docker build -t sampleapp .

docker rm -f samplerunning 2>/dev/null

docker run -d \
  --name samplerunning \
  -p 5050:5050 \
  sampleapp
