# This a Guess the number game.
# It ask the player their name and then ask them to guess a number between 1 and 20.
# It will either tell them their guess it too high or too low or they have guessed the number.
# The player will have 6 tries to guess the correct number.

import random

guesses_taken = 0

print("Welcome to Guess the Number game.")
print("What's your name?")
player_name = input()

number = random.randint(1, 20)
print("Well " + player_name + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")

while guesses_taken < 6:
  guess = int(input())

  guesses_taken += 1

  if guess == number:
    print("Good job " + player_name + "! You guessed the number in " + str(guesses_taken) + " guesses.")
    break

  if guess < number:
    print("Your guess is too low. Try again!")

  if guess > number:
    print("Your guess is too high. Try again!")

if guess != number:
  print("Sorry " + player_name + "! The number I was thinking of was " + str(number) + ".")
