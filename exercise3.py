# Part3 OOP Project

from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck ():
  def __init__(self):
    self.deck = [(s, r) for s in SUITE for r in RANKS]
  
  def shuffle(self):
    shuffle(self.deck)
  
  def split_in_half(self):
    return (self.deck[:26], self.deck[26:])

class Hand():
  def __init__(self, cards):
    self.cards = cards
  
  def __str__(self):
    return "Contains {} cards".format(len(self.cards))
  
  def add(self, added_cards):
    self.cards.extend(added_cards)
  
  def remove_card(self):
    return self.cards.pop()

class Player():
  def __init__(self, name, hand):
    self.name = name
    self.hand = hand
  
  def play_card(self):
    drawn_card = self.hand.remove_card()
    print("{} has placed: {}".format(self.name, drawn_card))
    print("\n")
    return drawn_card
  
  def remove_war_cards(self):
    war_cards = []
    if len(self.hand.cards) < 3:
      return self.hand.cards
    else:
      for x in range(3):
        war_cards.append(self.hand.remove_card())
      return war_cards
    
  def still_has_cards(self):
    return len(self.hand.cards) != 0
  

print("Welcome to War, let's begin...")

newdeck = Deck()

newdeck.shuffle()

half1, half2 = newdeck.split_in_half()

computer_player = Player("computer", Hand(half1))
name = input("What is your name?")
human_player = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while human_player.still_has_cards() and computer_player.still_has_cards():
  total_rounds += 1
  print("Time for a new round!")
  print("Here are the current standings")
  print(human_player.name + " has the count: " + str(len(human_player.hand.cards)))
  print(computer_player.name + " has the count: " + str(len(computer_player.hand.cards)))
  print("Play a card!")
  print("\n")

  table_cards = []
  comp_card = computer_player.play_card()
  human_card = human_player.play_card()

  table_cards.append(comp_card)
  table_cards.append(human_card)

  if comp_card[1] == human_card[1]:
    war_count += 1

    print("WAR!")
    table_cards.extend(human_player.remove_war_cards())
    table_cards.extend(computer_player.remove_war_cards())

    if RANKS.index(comp_card[1]) < RANKS.index(human_card[1]):
      human_player.hand.add(table_cards)
    else:
      computer_player.hand.add(table_cards)
  
  else:
    if RANKS.index(comp_card[1]) < RANKS.index(human_card[1]):
      human_player.hand.add(table_cards)
    else:
      computer_player.hand.add(table_cards)

print("Game over, number of rounds: " + str(total_rounds))
print("A war happened " + str(war_count) + " times")
print("Does the computer still have cards?")
print(str(computer_player.still_has_cards()))
print("Does the human player still have cards?")
print(str(human_player.still_has_cards()))