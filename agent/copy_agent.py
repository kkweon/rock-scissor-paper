import random
from typing import Optional

from model import Hand

from .agent import Agent


class CopyAgent(Agent):
    def get_hand(self, prev: Optional[Hand]) -> Hand:
        if prev is None:
            return random.choice([Hand.ROCK, Hand.SCISSOR, Hand.PAPER])
        return prev
