import random

randNum = random.randint(1, 10)
player_name = input("Hello. What is your name?")
num_Guesses = 0
print("Ok. Player " + player_name + "I am guessing numbers between 1 and 10")

while num_Guesses < 5:
  guess = int(input())
  num_Guesses += 1
  if guess < randNum:
    print("Your guess is too low")
  if guess > randNum:
    print("Your guess is too high")
  if guess == randNum:
    break 

if guess == randNum:
  print("Congratulations. You guessed number in " + str(num_Guesses) + "tries")
else:
  print("You did not guess. The number was " + str(randNum))


  