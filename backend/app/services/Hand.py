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
        self.sum = 0
        self.soft = False
        self.bet = bet
        # consider keeping Ace_count: for purposes of keeping track of soft hand status when removing aces from hand

    def add(self, card):
        self.card_list.append(card)
        self.sum += Hand.card_values[card.value]
        # handle soft hand
        if self.sum > 21:
            if self.soft:
                self.soft = False
                self.sum -= 10
            # else bust
        elif card.value == "Ace" and self.sum <= 11:
            self.sum += 10
            self.soft = True
    
    def pop_card(self): # Currently for split_hand use only
        extra_card = self.card_list.pop()
        self.sum -= Hand.card_values[extra_card.value]
        
        return extra_card
                     
    def split_hand(self):
        #split 1 hand with 2 cards into 2 hands with 1 card
        if len(self.card_list) != 2:
            print('can not split hand that is not size == 2')
            return None
        if self.card_values[self.card_list[0].value] != self.card_values[self.card_list[1].value]:
            print('can not split different value cards')
            return None
        new_hand = Hand(self.bet)
        extra = self.pop_card()
        new_hand.add(extra)
        return new_hand

    def get_valid_actions(self):
        valid_actions = []
        if self.sum < 21:
            valid_actions.append("hit")
            valid_actions.append("stand")
        if len(self.card_list) == 2:
            valid_actions.append("double")
            if self.card_values[self.card_list[0].value] == self.card_values[self.card_list[1].value]:
                valid_actions.append("split")
        return valid_actions
    
    def get_hand_values(self):
        hands = []
        for card in self.card_list:
            hands.append(card.value)
        return hands