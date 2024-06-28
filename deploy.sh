#!/bin/bash

# Variables
GIT_REPO_URL="https://github.com/Boltuzamaki/Portfolio.git"
DOCKER_IMAGE_NAME="portfolio_web"
CONTAINER_NAME="portfolio_web"

# Pull the latest code from the Git repositorydd
git pull origin main

# 
docker-compose down

# Build the Docker imaged
docker-compose up --build

echo "Deployment completed successfully."
