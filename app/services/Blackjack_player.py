import pydealer
from collections import deque
from Hand import Hand

class Blackjack_player:
    def __init__(self, bankroll, dealer_behavior = 'H17'):
        # store game state
        match dealer_behavior:
            case 'S17':
                self.dealer_behavior = 'S17'
            case _:
                self.dealer_behavior = 'H17'
        self.bankroll = bankroll
        self.players = deque() # deque of hands
        self.final_hands = []
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
        
    def play(self, bet_list = [100]):
        # deal player hand and dealer hand from deck
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
        while self.players:
            player = self.players.popleft()
            self.resolve_player(player)
        self.resolve_dealer()
        self.resolve_bets()
        
    def resolve_bets(self):
        for player in self.final_hands:
            # if blackjack
            if player.sum == 21 and player.size == 2:
                if (self.dealer.sum == 21 and self.dealer.size == 2):
                    self.bankroll += player.bet
                    print('push')
                    self.display_bankroll()
                else:
                    self.bankroll += player.bet*2.5 #blackjack
                    print('Blackjack!')
                    self.display_bankroll()
            elif self.dealer.sum == 21 and self.dealer.size == 2:
                print('lose')
                self.display_bankroll()
                return #lose
            elif player.sum > 21:
                print('lose')
                self.display_bankroll()
                return # lose bet
            elif self.dealer.sum > 21:
                self.bankroll += player.bet*2
                print('win')
                self.display_bankroll()
            elif player > self.dealer.sum:
                print('win')
                self.bankroll += player.bet*2
                self.display_bankroll()
            elif player < self.dealer.sum:
                print('lose')
                self.display_bankroll()
                return #lose
            elif player.sum == self.dealer.sum:
                print('push')
                self.bankroll += player.bet
                self.display_bankroll()
        return
        
    def get_player_action(self):
        # ask player for their choice of action
        # temporarily text input #TODO
        action = None
        while not action:
            action = input("Hit or Stand: ")
            match action:
                case 'hit':
                    return action
                case 'stand':
                    return action
                case 'double':
                    return action
                case 'split':
                    return action
                case _:
                    action = None
                    print('invalid action')
        
    
    def resolve_dealer(self):
        # automatically play for dealer
        # H17 rules OR S17 Rules
        while self.dealer.sum < 17:
            self.hit(self.dealer)
            if self.dealer_behavior == 'H17' and self.dealer.soft and self.dealer.sum == 17:
                self.hit(self.dealer)
        return
    
    def resolve_player(self, player:Hand):
        while player.sum < 21:
            action = self.get_player_action()
            match action:
                case 'hit':
                    self.hit(player)
                case 'stand':
                    self.stand(player)
                case 'double':
                    self.double(player)
                case 'split':
                    self.split(player)
        
    def hit(self, player):
        player.add(self.shoe.deal(1)[0])
        return

    def stand(self, player):
        # add hand to final_hands
        self.final_hands.append(player)
        return

    def double(self, player):
        # double bet
        self.bankroll -= player.bet
        player.bet = player.bet*2
        # immediately hit and stand
        self.hit(player)
        self.stand(player)
        return

    def split(self, player):
        # split into two players
        # deal 1 card to each player
        # add second player to deque
        # continue play of first player
        pass #TODO # requires functionality in Hand class
    
    def display_bankroll(self):
        print('Current bankroll: ', self.bankroll)
        return

if __name__ == "__main__":
    game = Blackjack_player(1000)
    game.play([100])