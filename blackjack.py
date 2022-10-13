import random

# outline my classes and set some constants
SUITS = ['♥️', '♠️', '♦️', '♣️']
RANK_VALUES = {
    'A': (11, 1),
    # TODO: handle when ace is 1 or 11, start with 1
    'K': 10,
    'Q': 10,
    'J': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10
}


class Game:
    # making a new deck of cards in order to play the game which calls __init__ method
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        # deal two cards to each player to start game
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.player)
        # self is whatever instance of the class we are dealing with in the________?

        print("The dealer's cards are: ")
        for card in self.dealer.hand:
            print(card)
        print(f"The dealer's hand is worth {self.calculate_hand(self.dealer)}")

        print("The player's cards are: ")
        for card in self.player.hand:
            print(card)
        print(f"This player's hand is worth {self.calculate_hand(self.player)}")

        print(f"There are now {len(self.deck.cards)} reamaining the deck.")

    def deal_card(self, participant):
        # take ONE card from the deck and deal to participant's hand
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            if card.rank == "A":
                total_points += card.value
                if total_points > 21:
                    total_points -= 10
            else:
                total_points += card.value

            total_points += card.value
        return total_points



    # below will be the function that deals the cards
    def deal(self):
        pass
        # deck shuffled and each player dealt two cards
        # cards are dealt one up one down such that the
        # player only sees one card of dealer hand
        # won't see until cards faced up at end of game
        # on first hand player both hands must be checked for 21
        # each turn player can hit/stay/split w/conditions for each
        # input do you want to hit or stay or split(not base game)
        # based on response (1)another card will be dealt (2)no card is dealt (3)the hand will be split and two cards will be dealt 
        # if hit => hand checked for value
        # if value > 21 'bust', ==21 'win with 21', <21 input hit or stay
        # game ends when a player reaches 21 or both players bust


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# example of building one card
# queen_of_hearts=Card('heart', 'Q', 10)
# print(f'{queen_of_hearts} is worth {queen_of_hearts.value}')


# building whole deck
class Deck:
    def __init__(self):
        self.cards = []
        # self.used = False --not entirely sure how/if to use this
        for suit in SUITS:
            for rank_value in RANK_VALUES.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)
                # could also do self.cards.append(Card(suit, rank_value[]))?
        self.shuffle()

    def __str__(self):
        return f'This deck has {len(self.cards)} cards'

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.hand = []


class Player:
    def __init__(self):
        self.hand = []
        # below tab9 popped up this AI so just keeping for reference/help
        # to see how complex vs. our simpler game
        # class Player:
        #     def __init__(self, name):
        #         self.name = name
        #         self.score = 0
        #         self.winning = False
        #         self.is_win = False
        #         self.is_draw = False


# INSTANCIATES the game => by calling the __init__ method
def play_game():
    # TODO make player go first
    if new_game.calculate_hand(new_game.dealer) == 21:
        # dealer has blackjack
        print("Dealer has Blackjack!")
        # dealer and player both have blackjack
        if new_game.calculate_hand(new_game.player) == 21:
                print("Push")
                return
        else:
            print(f"Player loses with {new_game.calculate_hand(new_game.player)}")
            return
    elif new_game.calculate_hand(new_game.player) == 21:
        print("Blackjack! Player wins!")
        return

    while new_game.calculate_hand(new_game.dealer) < 17:
        new_game.deal_card(new_game.dealer)
        print("Dealer hits.")
        print("Dealer's hand is: ")
        [print(card) for card in new_game.dealer.hand]

        if new_game.calculate_hand(new_game.dealer) == 21:
            print("Dealer has 21!")
        elif new_game.calculate_hand(new_game.dealer) > 21:
            print(f"Dealer busts with {new_game.calculate_hand(new_game.dealer)}!")
            break
    # we reach this else only if the 17 < dealer hand <21
    else:
        print("Dealer's hand is: ")
        [print(card) for card in new_game.dealer.hand]
        # this list comprehension is shorthand for 
        # for card in new_game.dealer.hand:
        # print(card)
        print(f"Dealer stays with {new_game.calculate_hand(new_game.dealer)}.")
        print("Player's hand is: ")
        [print(card) for card in new_game.player.hand]
        print(f"Player has {new_game.calculate_hand(new_game.player)}")
        choice = ""
        while choice != "s":
            choice = input("Would you like to (h)it or (s)tay?").lower()
        if choice == "h":
            new_game.deal_card(new_game.player)
            print("Player's hand is: ")
            [print(card) for card in new_game.player.hand]
            print(f"Player has {new_game.calculate_hand(new_game.player)}")

        if choice != "s":
            print("Please enter 'h' for hit or 's' for stay")
        # print(f"Dealer's stays with {new_game.dealer.calculate_hand}.")
        print("Player's hand is: ")

new_game = Game()
play_game ()
