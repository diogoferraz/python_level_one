# Rules of the game
# The computer will think of 3 digits number that has no repeating digits.
# You will then guess a 3 digit number
# The computer will then give back clues
# Based on these clues you will guess again until you break the code with a matching number

# Clues
# Close: You've guessed a correct number but in the wrong position
# Match: You've guessed a correct number in the correct position
# Nope: You haven't guess any of the numbers correctly
import random

# GET GUESS
def get_guess():
  return list(input("What is your guess? "))

# GENERATE COMPUTER CODE
def generate_code():
  digits = [str(num) for num in range(10)]
  # Shuffle the digits
  random.shuffle(digits)
  # Then grab the first 3
  return digits[:3]

# GENERATE THE CLUES
def generate_clues(code, user_guess):
  if user_guess == code:
    return "CODE CRACKED!"

  clues = []

  for ind, num in enumerate(user_guess):
    if num == code[ind]:
      clues.append("Match")
    elif num in code:
      clues.append("Close")
  
  if clues == []:
    return ["Nope"]
  else:
    return clues

# RUN GAME LOGIC
  
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

secret_code = generate_code()
clue_report = []

while clue_report != "CODE CRACKED!":
  guess = get_guess()
  clue_report = generate_clues(guess, secret_code)
  print("Here is the result of your guess: ")
  for clue in clue_report:
    print(clue)