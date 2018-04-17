import unittest
import cards.deck

class TestDeck(unittest.TestCase):

    def test_shuffle(self):
        deck = cards.deck.CardList()
        initial_deck = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(initial_deck, deck.cards)

    def test_deal_direct(self):
        for number_of_cards in range(0, 52):
            deck = cards.deck.CardList()
            hand = cards.deck.CardList([])
            hand.take(deck.give(number_of_cards))
            self.assertEqual(hand.count, number_of_cards)
            self.assertEqual(deck.count, 52 - number_of_cards)

    def test_deal_direct_neg_cards(self):
        deck = cards.deck.CardList()
        hand = cards.deck.CardList([])
        hand.take(deck.give(-5))
        self.assertEqual(hand.count, 0)
        self.assertEqual(deck.count, 52)

    def test_deal_direct_too_many_cards(self):
        deck = cards.deck.CardList()
        hand = cards.deck.CardList([])
        hand.take(deck.give(100))
        self.assertEqual(hand.count, 52)
        self.assertEqual(deck.count, 0)

    def test_deck_json_round_trip(self):
        deck = cards.deck.CardList()
        new_deck = cards.deck.CardList()
        new_deck.from_json(deck.to_json())
        self.assertEqual(deck, new_deck)

class TestCards(unittest.TestCase):

    def test_card_json(self):
        card = cards.deck.Card("Hearts", "Queen")
        new_card = cards.deck.Card()
        new_card.from_json(card.to_json())
        self.assertEqual(card, new_card)