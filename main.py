from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, HTTPException, status
from enums import ServiceBusTopics

from config import settings
from models import MapalEventPayload, MindsmithEventPayload
from publisher import ServiceBusPublisher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("simple_webhook_servicebus")

publisher = ServiceBusPublisher(
    settings.service_bus_connection_string,
)


@asynccontextmanager
async def lifespan(_):
    publisher.initialize()
    try:
        yield
    finally:
        publisher.close()


app = FastAPI(
    title="Simple Webhook Service Bus Producer",
    description=(
        "Receives webhook payloads and forwards them to an Azure Service Bus topic."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

@app.post(
    "/webhook/mos",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["mos"]
)
async def mos_pub(
    payload: MapalEventPayload,
):
    logger.info("Received webhook payload")

    try:
        publisher.publish(
            ServiceBusTopics.mos.value,
            payload.event_type,
            payload.message
        )
    except Exception as exc:
        logger.exception("Webhook processing failed")
        raise HTTPException(status_code=500, detail=f"Publish failed: {exc}") from exc

    return {"status": "accepted"}

@app.post(
    "/webhook/mindsmith",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["mindsmith"]
)
async def mindsmith_pub(
    payload: MindsmithEventPayload,
):
    logger.info("Received webhook payload")

    try:
        publisher.publish(
            ServiceBusTopics.mindsmith.value,
            payload.type,
            payload.model_dump()
        )
    except Exception as exc:
        logger.exception("Webhook processing failed")
        raise HTTPException(status_code=500, detail=f"Publish failed: {exc}") from exc

    return {"status": "accepted"}
