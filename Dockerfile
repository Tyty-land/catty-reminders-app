FROM python:3.10-slim

WORKDIR /app

COPY requirements-prod.txt .

RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

EXPOSE 8181

ARG DEPLOY_REF=NA
ENV DEPLOY_REF=$DEPLOY_REF

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8181"]
