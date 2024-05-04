from enum import IntEnum
from collections import deque
import random

import pandas as pd

class Gem(IntEnum):
    RUBY = 0
    SAPPHIRE = 1
    DIAMOND = 2
    EMERALD = 3
    ONYX = 4
    JOKER = 5

    @staticmethod
    def color_to_gem(color: str):
        return {
            "red": Gem.RUBY,
            "blue": Gem.SAPPHIRE,
            "white": Gem.DIAMOND,
            "green": Gem.EMERALD,
            "black": Gem.ONYX,
        }[color.lower()]

class Card:
    def __init__(self):
        self.points = 0
        self.color = None
        self.cost = [0 for _ in range(len(Gem)-1)]

class Deck:
    def __init__(self):
        self.cards = deque()

    def shuffle(self):
        random.shuffle(self.cards)


class GemBank:
    def __init__(self):
        self.gems = [7 for _ in range(len(Gem))]
        self.gems[Gem.JOKER] = 6

class Player:
    MAX_RESERVED_CARDS = 3
    MAX_GEMS = 10
    N_SAME_GEM_TO_TAKE = 2
    N_DIFFERENT_GEMS_TO_TAKE = 3

    def __init__(self):
        self.stash = [0 for _ in len(Gem)]
        self.cards = []
        self.reserved_cards = 0
        self.points = 0

    def take_gems(self):
        pass

    def take_same_gem(self):
        pass

    def take_different_gems(self):
        pass

    def reserve_card(self):
        pass

    def buy_cards(self):
        pass

    def discard_excess_gems(self):
        while sum(self.stash) > MAX_GEMS:
            pass


if __name__ == "__main__":

    decks = {}
    df = pd.read_csv("cards.csv")
    non_color_cols = ['Level', 'Color', 'PV']
    color_cols = set(df.columns) - set(non_color_cols)
    for v, g in df.groupby("Level"):
        decks[v] = Deck()
        for ind, row in g.iterrows():
            new_card = Card()
            new_card.points = row["PV"]
            new_card.color = Gem.color_to_gem(row["Color"])
            
            for c in color_cols:
                new_card.cost[Gem.color_to_gem(c)] = row[c]
            decks[v].cards.append(new_card)

        decks[v].shuffle()

    for ind, deck in decks.items():
        print(f"Deck {ind}")
        for c in deck.cards:
            print(c.cost)
