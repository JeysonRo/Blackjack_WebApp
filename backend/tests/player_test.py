import pydealer

def test_hand_persists_between_deals():
    shoe = pydealer.Deck()

    shoe.shuffle()
    hand = shoe.deal(1)
    hand = shoe.deal(1)
    assert len(hand) == 2, "Hand is not length 2!"