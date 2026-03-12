# Service Bus Producer & Emulator

Local webhook service that publishes messages to the Azure Service Bus Emulator.

## Prerequisites
- Docker

## Setup

### Clone the repository:

`git clone https://github.com/pmissagia/servicebus-emulator.git`

### Start the environment:

`docker compose up -d --build`

NOTE: This will start the following containers:
- servicebus-producer
- servicebus-emulator
- mssql

### Swagger

`http://localhost:8005/docs`

### API

```
POST /webhook/mos
{
  "event_type": "string",
  "message": {}
}
```

```
POST /webhook/mindsmith
{
  "type": "string",
  "placement_id": "uuid",
  "tenant_id": "uuid",
  "data": {}
}
```
