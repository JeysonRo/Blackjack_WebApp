import pydealer

def test_hand_persists_between_deals():
    shoe = pydealer.Deck()

    deck.shuffle()
    hand = deck.deal(1)
    hand = deck.deal(1)
    assert len(hand) == 2, "Hand is not length 2!"