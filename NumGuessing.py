import random

attempts_list = []
def showScore():
  if len(attempts_list) <= 0:
    print("There is no score for now.")
  else:
    print("The current score is {} attempts".format(min(attempts_list)))

def startGame():
  rand_Num = int(random.randint(1, 10))
  print("###################################")
  print("Hello player.")
  player_name = input("Enter your name:")
  wanna_play = input("Hi {}, would you like to play number guessing game?".format(player_name))
  attempts = 0
  showScore()

  while wanna_play.lower() == "yes":
    try:
      guess = input("Pick a number between 1 and 10")
      if(int(guess) < 1 or int(guess) > 10):
        raise ValueError("Please guess a number in given range")
      if(int(guess) == rand_Num):
        print("You guessed random number")
        attempts += 1 
        attempts_list.append(attempts)
        print("It took you {} attempts to guess".format(attempts))
        play_again = input("Hi {} would you like to play again?".format(player_name))
        attempts = 0
        showScore()
        rand_Num = int(random.randint(1, 10))
        if(play_again.lower() == "no"):
          print("OK. Have a nice day")
          break 
      elif(int(guess) > rand_Num):  
        print("Number is lower")
        attempts += 1
      elif(int(guess) < rand_Num):
        print("Number is higher")
        attempts += 1 
    except ValueError as err:
      print("That is not a valid number.")
      print("({}".format(err))
  else:
    print("Ok.")

if __name__ == "__main__":
  startGame()





