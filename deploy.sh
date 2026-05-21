#!/bin/bash
exec > /home/ubu/deploy.log 2>&1
set -x

BRANCH=${1:-lab1}

cd /home/ubu/app-code

git fetch origin

git checkout -B "$BRANCH" "origin/$BRANCH"
git reset --hard "origin/$BRANCH"

sudo systemctl restart catty-app.service
