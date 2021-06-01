from joule.providers import BaseProvider, Event
from mypy_boto3_autoscaling.client import AutoScalingClient as AutoScalingClient
from mypy_boto3_sqs.client import SQSClient as SQSClient
from mypy_boto3_sqs.service_resource import Message as Message, Queue as Queue
from typing import Any, Iterator, Optional

class AwsProvider(BaseProvider):
    instance_id: Any = ...
    queue: Any = ...
    asg: Any = ...
    def __init__(self, *applications: object) -> None: ...
    def mark_essential(self) -> None: ...
    def get_events_from_message_queue(self) -> Iterator[Optional[Event]]: ...
    def send_join_to_message_queue(self, application: object, event: Event, payload: dict) -> None: ...
