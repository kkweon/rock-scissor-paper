import pytest

from game import Game

from .copy_agent import CopyAgent
from .user_agent import UserAgent


@pytest.mark.skip(reason="Make this test pass")
def test_user_agent_can_beat_copy_agent():
    user_agent = UserAgent()
    copy_agent = CopyAgent()

    g = Game(user_agent, copy_agent)
    winner = g.play(5)

    assert winner is user_agent
