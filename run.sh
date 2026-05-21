#!/bin/bash
cd /home/ubu/app-code
export DEPLOY_REF=$(git rev-parse HEAD)
exec /home/ubu/app-venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8181
