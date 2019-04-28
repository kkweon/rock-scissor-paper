"""
Complete UserAgent.get_hand() Function
"""
from typing import Optional

from model import Hand

from .agent import Agent


class UserAgent(Agent):
    def get_hand(self, prev: Optional[Hand]) -> Hand:
        """Returns a Hand

        Args:
            prev (Optional[Hand]):
                An opponent's hand in the previous round.
                It will be None if it's the first round
        """
        raise NotImplementedError
