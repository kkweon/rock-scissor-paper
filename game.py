from agent import Agent
from model import Hand


class Game:
    def __init__(self, p1: Agent, p2: Agent):
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def check_win(p1_hand: Hand, p2_hand: Hand) -> int:
        """
        If player1's hand wins, returns -1
        If draw, 0
        If player2's hand wins, 1
        """
        if p1_hand == p2_hand:
            return 0

        if p1_hand == Hand.ROCK and p2_hand == Hand.SCISSOR:
            return -1
        if p1_hand == Hand.SCISSOR and p2_hand == Hand.PAPER:
            return -1
        if p1_hand == Hand.PAPER and p2_hand == Hand.ROCK:
            return -1
        return 1

    def play(self, n_win: int) -> Agent:
        """
        Play until one player's win == n_win
        """
        p1_score = 0
        p2_score = 0

        # the p1's hand of previous round
        h1_prev = None
        h2_prev = None

        while p1_score < n_win or p2_score < n_win:
            # give previous hand
            h1 = self.p1.get_hand(h2_prev)
            h2 = self.p2.get_hand(h1_prev)

            if Game.check_win(h1, h2) == -1:
                p1_score += 1
            elif Game.check_win(h1, h2) == 1:
                p2_score += 1

            h1_prev, h2_prev = h1, h2

        if p1_score == n_win:
            return self.p1
        return self.p2
