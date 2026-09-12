import pydealer
from collections import deque
from .Hand import Hand
        
class Blackjack_game:
    def __init__(self, bankroll, dealer_behavior = 'H17', deck_count = 4, deck_pen = 21):
        # store game state
        match dealer_behavior:
            case 'S17':
                self.dealer_behavior = 'S17'
            case _:
                self.dealer_behavior = 'H17'
        self.bankroll = bankroll
        self.players:deque[Hand] = deque() # deque of hands
        self.final_hands:list[Hand] = []
        self.dealer = Hand()
        
        self.deck_pen = deck_pen
        self.deck_count = deck_count
        self.initialize_shoe(deck_count)
        
    def initialize_shoe(self, deck_count: int):
        self.shoe = pydealer.Deck(rebuild=False)
        for i in range(1, deck_count):
            self.shoe.build() # adds a 52 card deck to the stack
        self.shoe.shuffle()
        return self.shoe
        
    def play(self, bet_list = [100]):
        # rebuild shoe if deck_pen reached
        if self.shoe.size <= self.deck_pen:
            self.initialize_shoe(self.deck_count)
        # deal player hand and dealer hand from deck
        self.players:deque[Hand] = deque()
        self.final_hands:list[Hand] = []
        self.dealer = Hand()
        for i in range(len(bet_list)):
            self.players.append(Hand(bet_list[i]))
            self.bankroll -= bet_list[i]
        self.hit(self.dealer)
        for player in self.players:    
            self.hit(player)
        self.hit(self.dealer)
        for player in self.players:    
            self.hit(player)
        
        
        # action on player
        print("Dealer:", self.dealer.card_list[1])
    
    def resolve_dealer(self):
        # automatically play for dealer
        # H17 rules OR S17 Rules
        while self.dealer.sum < 17:
            self.hit(self.dealer)
            if self.dealer_behavior == 'H17' and self.dealer.soft and self.dealer.sum == 17:
                self.hit(self.dealer)
        print("Dealer sum:", self.dealer.sum)
        return
        
    def hit(self, player):
        if self.shoe.size == 0:
            self.initialize_shoe(self.deck_count)
        player.add(self.shoe.deal(1)[0])
        return

    def stand(self, player):
        # add hand to final_hands
        self.players.popleft()
        self.final_hands.append(player)
        if not self.players:
            self.resolve_dealer()
        return

    def double(self, player):
        # double bet
        self.bankroll -= player.bet
        player.bet = player.bet*2
        # immediately hit and stand
        self.hit(player)
        self.stand(player)
        return

    def split(self, player: Hand):
        # split into two players
        second_hand = player.split_hand()
        if not second_hand:
            return
        self.bankroll -= player.bet
        # deal 1 card to each player
        self.hit(player)
        self.hit(second_hand)
        # add second player to deque
        self.players.appendleft(second_hand)
        # continue play of first player
        return
    
    def display_bankroll(self):
        print('Current bankroll: ', self.bankroll)
        return

if __name__ == "__main__":
    game = Blackjack_game(1000)