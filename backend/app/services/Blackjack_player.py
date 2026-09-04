import pydealer
from collections import deque
from .Hand import Hand
        
class Blackjack_game:
    def __init__(self, bankroll, dealer_behavior = 'H17'):
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
        self.initialize_shoe()
        
    def initialize_shoe(self):
        self.shoe = pydealer.Deck(rebuild=True, re_shuffle=True)
        self.shoe.shuffle()
        return self.shoe
        
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
        print("Dealer:", self.dealer.card_list[1])
        
        # won't be used for web version
        
        # while self.players:
        #     player = self.players.popleft()
        #     self.resolve_player(player)
        
        # self.resolve_dealer()
        # self.resolve_bets()
        
    def resolve_bets(self):
        player: Hand
        for player in self.final_hands:
            # if blackjack
            if player.sum == 21 and len(player.card_list) == 2:
                if (self.dealer.sum == 21 and len(self.dealer.card_list) == 2):
                    self.bankroll += player.bet
                    print('push')
                    self.display_bankroll()
                else:
                    self.bankroll += player.bet*2.5 #blackjack
                    print('Blackjack!')
                    self.display_bankroll()
            elif self.dealer.sum == 21 and len(self.dealer.card_list) == 2:
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
            elif player.sum > self.dealer.sum:
                print('win')
                self.bankroll += player.bet*2
                self.display_bankroll()
            elif player.sum < self.dealer.sum:
                print('lose')
                self.display_bankroll()
                return #lose
            elif player.sum == self.dealer.sum:
                print('push')
                self.bankroll += player.bet
                self.display_bankroll()
        return
        
    def get_player_action(self, player: Hand, action = None):
        # ask player for their choice of action
        # temporarily text input
        while not action:
            if len(player.card_list) == 2: # can double
                if player.card_list[0] == player.card_list[1]: # player can split
                    print("Options: Hit | Stand | Double | Split")
                else:
                    print("Options: Hit | Stand | Double")
            else:
                print("Options: Hit | Stand")
            
            if not action: action = input()
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
        print("Dealer sum:", self.dealer.sum)
        return
    
    def resolve_player(self, player:Hand):
        print("next player")
        while player.sum < 21:
            print("Current hand sum:", player.sum)
            action = self.get_player_action(player)
            match action:
                case 'hit':
                    self.hit(player)
                case 'stand':
                    self.stand(player)
                    break
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
    game.play([100,100,100])