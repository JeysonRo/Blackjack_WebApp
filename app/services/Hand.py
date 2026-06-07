import pydealer

class Hand:
    card_values = {"Ace" : 1,
                    "2" : 2,
                    "3" : 3,
                    "4" : 4,
                    "5" : 5,
                    "6" : 6,
                    "7" : 7,
                    "8" : 8,
                    "9" : 9,
                    "10" : 10,
                    "Jack" : 10,
                    "Queen" : 10,
                    "King" : 10}
    
    def __init__(self, bet:int = 100):
        self.card_list = []
        self.size = 0
        self.sum = 0
        self.soft = False
        self.bet = bet

    def add(self, card):
        self.card_list.append(card)
        self.size += 1
        self.sum += Hand.card_values[card.value]
        # handle bust and Ace
        if self.sum > 21:
            if self.soft:
                self.soft = False
                self.sum -= 10
            # else bust
        elif card.value == "Ace" and self.sum <= 11:
            self.sum += 10
            self.soft = True
                     
    def split(self):
        # TODO split 2 cards into 2 hands
        pass