import logging

from abc import ABC, abstractmethod

from autoscale.events import Events, Event
from autoscale.providers import BaseProvider


class BaseApplication(ABC):
    """
    Base Application class.

    Inherit for shared methods.
    """

    @abstractmethod
    def join(self, provider: BaseProvider, event: Event) -> None:
        return

    @abstractmethod
    def launch(self, provider: BaseProvider, event: Event) -> None:
        return

    @abstractmethod
    def terminate(self, provider: BaseProvider, event: Event) -> None:
        return