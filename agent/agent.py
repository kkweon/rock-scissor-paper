import abc
from typing import Optional

from model import Hand


class Agent(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_hand(self, prev: Optional[Hand]) -> Hand:
        raise NotImplemented
