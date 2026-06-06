import pydealer
from Hand import Hand

class Blackjack_player:
    def __init__(self, bankroll):
        # store game state
        self.bankroll = bankroll
        self.player = None
        self.dealer = None
        # ^ may replace with self.players = []
        # list of players for multiple hands
        # maybe necessary to implement split
        self.shoe = pydealer.Deck(rebuild=True, re_shuffle=True)
        self.shoe.shuffle()
        
    def initialize_shoe(self):
        shoe = pydealer.Deck(rebuild=True, re_shuffle=True)
        self.shoe.shuffle()
        return shoe
        
    def bet(self, bet_amount = 0):
        self.bankroll -= bet_amount
        # deal player hand and dealer hand from deck
        self.dealer = Hand()
        self.player = Hand()
        self.hit(self.dealer)
        self.hit(self.player)
        self.hit(self.dealer)
        self.hit(self.player)
        # action on player
        while self.player.sum < 21:
            action = get_player_action()
            match action:
                case 'hit':
                    self.hit(self.player)
                case 'stand':
                    self.stand(self.player)
                case 'double':
                    self.double(self.player)
                case 'split':
                    self.split(self.player)
        self.resolve_dealer()
        # if blackjack and not dealer blackjack
        if self.player.sum == 21 and self.player.size == 2:
            if (self.dealer.sum == 21 and self.dealer.size == 2):
                self.bankroll += bet_amount
            else:
                self.bankroll += bet_amount*2.5 #blackjack
        elif self.dealer.sum == 21 and self.dealer.size == 2:
            return #lose
        elif self.player.sum > 21:
            return # lose bet
        elif self.dealer.sum > 21:
            self.bankroll += bet_amount*2
        elif self.player > self.dealer.sum:
            self.bankroll += bet_amount*2
        elif self.player < self.dealer.sum:
            return #lose
        elif self.player.sum == self.dealer.sum:
            self.bankroll += bet_amount
            
        return
        
    def get_player_action(self):
        # ask player for their choice of action
        pass #TODO
    def resolve_dealer(self):
        # automatically play for dealer
        # H17 rules OR S17 Rules
        pass #TODO
        
    def hit(self, hand):
        hand.add(self.shoe.deal(1)[0])

    def stand(self):
        pass #TODO

    def double(self):
        pass #TODO

    def split(self):
        pass #TODO

if __name__ == "__main__":
    game = Blackjack_player(1000)
    game.bet(100)