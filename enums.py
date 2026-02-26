from enum import Enum


class ServiceBusTopics(str, Enum):
    mindsmith = "mindsmith.topic"
    mos = "mos.topic"
