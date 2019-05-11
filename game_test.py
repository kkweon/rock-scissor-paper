from agent import RandomAgent
from game import Game
from model import Hand


def test_rock_wins_sccissor():
    assert Game.check_win(Hand.ROCK, Hand.SCISSOR) == -1


def test_rock_loses_paper():
    assert Game.check_win(Hand.ROCK, Hand.PAPER) == 1


def test_rock_draws_rock():
    assert Game.check_win(Hand.ROCK, Hand.ROCK) == 0


def test_paper_wins_rock():
    assert Game.check_win(Hand.PAPER, Hand.ROCK) == -1


def test_game_plays():
    a1 = RandomAgent()
    a2 = RandomAgent()

    g = Game(a1, a2)
    winner = g.play(3)
    assert a1 is winner or a2 is winner
