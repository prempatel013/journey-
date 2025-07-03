# Project 3: Number Guessing Game 🎮
# Concepts Used: Loops, conditionals, random numbers

number=3
attempts=4

ask=input("Do you want to play this game? (yes/no): ")


if ask!="yes":
    quit()

while attempts > 0:
    ask=input("guess the number between (1-10)and you have only 4 attemps to try :")
    if ask == number:
        print("You won!")

        break
    attemps-=1
else:
        print("wrong try again.....")
      
       
    


  