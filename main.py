import art
import random
print(art.logo)


def game():
  start_game = False
  while start_game == False:
    want_to_play = input("Welcome to Guess The Number. Would you like to play? 'y' or 'n': ")
    if want_to_play == 'y':
      start_game = True
      winning_number = random.randint(0, 100)
      attempts = 0
      while start_game == True:
        difficulty = input("Would you like to play easy or hard mode? 'e or h' ")
        if difficulty == "e":
          attempts = 10
          print(f"{10} attempts remaining.")
        else:
          attempts = 5
          print(f"{5} attempts remaining.")
    
        number_guessed = input("Guess a number between 0-100: ")
  
        if int(number_guessed) == winning_number:
          print("You Win! ")
          start_game = False
  
        while int(number_guessed) != winning_number:
        
          if int(number_guessed) < winning_number:
            attempts -= 1
            if attempts > 0:
              print(f"{attempts} attempts remaining.")
              number_guessed = input("Too Low. Guess Again: ")
  
            if attempts == 0:
              print("You Ran Out of Turns You Lose! ")
              start_game = False
              print(f"the winning number was {winning_number}")
  
            if int(number_guessed) == winning_number:
              print("You Win! ")
              start_game = False
           
          if int(number_guessed) > winning_number:
            attempts -= 1
            if attempts > 0:
              print(f"{attempts} attempts remaining.")
              number_guessed = input("Too High. Guess Again: ")
  
            if attempts == 0:
              print("You Ran Out of Turns You Lose! ")
              start_game = False
              print(f"the winning number was {winning_number}")
    
            if int(number_guessed) == winning_number:
              print("You Win! ")
              start_game = False

    if want_to_play == 'n':
      start_game = True
      print("Come Back Later!")

game()
