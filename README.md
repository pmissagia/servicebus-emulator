# Simple Webhook Service Bus Producer

Minimal FastAPI service that accepts POST payloads and publishes them to an Azure Service Bus topic.

## Features

- Single custom endpoint: `POST /webhook`
- No request auth
- No payload schema validation
- Swagger UI available at `/docs`
- OpenAPI available at `/openapi.json`

## Required environment variables

- `SERVICE_BUS_CONNECTION_STRING`
- `SERVICE_BUS_TOPIC_NAME`

## Run locally

1. Create and activate a virtual environment
2. Install dependencies from `requirements.txt`
3. Copy `.env.example` to `.env` and set values
4. Run:

`uvicorn main:app --host 0.0.0.0 --port 8005 --reload`

## Run with Docker Compose

1. Copy `.env.example` to `.env` and set values
2. Run:

`docker compose up --build`

## Test webhook

Send a POST request to `http://localhost:8005/webhook` with JSON body.
