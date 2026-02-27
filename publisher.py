import logging
import json

from azure.servicebus import ServiceBusClient, ServiceBusMessage

logger = logging.getLogger("simple_webhook_servicebus")


class ServiceBusPublisher:
    def __init__(self, connection_string):
        if not connection_string:
            raise RuntimeError("Missing required value: SERVICE_BUS_CONNECTION_STRING")

        self.connection_string = connection_string
        self._client = None

    def initialize(self):
        if self._client is None:
            self._client = ServiceBusClient.from_connection_string(
                conn_str=self.connection_string
            )
            logger.info(
                "Service Bus client initialized"
            )

    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None

    def publish(self, topic, event_type, payload):
        sb_message = ServiceBusMessage(
            body=json.dumps(payload),
            application_properties={
                "event_type": event_type,
                "event": event_type,
            }

        )

        with self._client.get_topic_sender(
            topic_name=topic
        ) as sender:
            sender.send_messages(sb_message)

        logger.info("Message sent successfully")
