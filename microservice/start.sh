#!/bin/bash
cd Logging_and_tracing
docker-compose up -d
cd ..
docker-compose up --build 
