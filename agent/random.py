"""
Random Agent

Choose a random hand
"""
import random
from typing import Optional

from model import Hand

from .agent import Agent


class RandomAgent(Agent):
    def get_hand(self, prev: Optional[Hand]) -> Hand:
        return random.choice([Hand.ROCK, Hand.SCISSOR, Hand.PAPER])
