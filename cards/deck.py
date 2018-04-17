"""
Deck of cards.
"""
import itertools
import json
import random

SUITS = (
    'Hearts',
    'Diamonds',
    'Clubs',
    'Spades'
)
RANKS = [str(x) for x in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']


class Card(object):
    """
    A single card in a classic card deck.
    """
    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def to_json(self):
        """
        Return a string containing a JSON representation of a card.
        """
        return '{{"suit":"{}", "rank":"{}"}}'.format(self.suit, self.rank)

    def from_json(self, json_str):
        """
        Loads a card from a valid JSON representation.
        """
        card = json.loads(json_str)
        self.suit = card['suit']
        self.rank = card['rank']

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.suit == other.suit and self.rank == other.rank
        return False

    def __unicode__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__unicode__()


class CardList(object):
    """
    An ordered list of an arbitrary number of Card objects.
    """
    def __init__(self, card_list=None):
        """
        """
        if card_list is None:
            self.reset_to_standard()
        else:
            self.cards = card_list

    def reset_to_standard(self):
        """
        Form a full 52 card deck, ordered.
        """
        self.cards = [Card(s, r) for s, r in list(itertools.product(SUITS, RANKS))]

    def shuffle(self):
        """
        Shuffle the remaining cards in the deck.
        """
        for idx, card in enumerate(self.cards):
            new_idx = random.randrange(0, len(self.cards))
            tmp_card = self.cards[new_idx]
            self.cards[new_idx] = self.cards[idx]
            self.cards[idx] = tmp_card

    def give(self, num_cards):
        """
        Give out the specified number of cards, removing them from the deck.
        Cards are given from the top of the deck.
        """
        if num_cards < 0:
            return None
        given_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return given_cards

    def take(self, cards):
        """
        Takes a list of Card objects into this hand. Appends them to the end of the card list.
        """
        if isinstance(cards, list):
            for card in cards:
                if isinstance(card, Card):
                    self.cards.append(card)

    @property
    def count(self):
        """
        Returns the number of cards in the list.
        """
        return len(self.cards)

    def to_json(self):
        """
        Return a string containing a JSON representation of a card list.
        """
        return '[{}]'.format(','.join([card.to_json() for card in self.cards]))

    def from_json(self, json_str):
        """
        Loads a card list from a valid JSON representation.
        WARNING: Erases all existing cards in the list!
        """
        card_list = json.loads(json_str)
        self.cards = []
        for card in card_list:
            self.cards.append(Card(card['suit'], card['rank']))

    def __eq__(self, other):
        # if isinstance(other, self.__class__):
        if other.count == self.count:
            for idx in range(0, other.count):
                if self.cards[idx] != other.cards[idx]:
                    return False
            return True
        return False

    def __unicode__(self):
        return ':'.join(['{}{}'.format(c.suit[0], c.rank[0]) for c in self.cards])

    def __repr__(self):
        return self.__unicode__()
