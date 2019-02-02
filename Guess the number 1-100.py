import random
import time

print("Welcome to Guess the Number Between 1-100")
print(" ")

def main():
   while True:
      counter = 0

      time.sleep(1)

      random_number = random.randrange(1,100)

      player_guess = int(input("Guess the number between 1-100:"))

      while player_guess > 100:
         if player_guess > 100:
            print("Invalid input, please try again!")
            player_guess = int(input("Guess the number between 1-100:"))

      while True:

         if player_guess != random_number:
            print("")
            print("Wrong, Try Again!")
            print("")
            counter += 1
            print("Guess counter:",counter)
            if player_guess < random_number:
               print("The number you are look for is higher!")
               print(" ")
            elif player_guess > random_number:
               print("The number you ar looking for is lower!")
               print("")
            player_guess = int(input("Guess the number between 1-100:"))
         elif player_guess == random_number:
            print("")
            print("Correct! the number was", random_number)
            break

      print("You took",counter,"guess!")

      print("")

main()
