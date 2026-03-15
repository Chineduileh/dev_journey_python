##NUMBER GUESSING GAME USING CONTROL FLOW CONCEPTS.
import random
Target_number= random.randint(1,11) #Get random number for as guess target.
Number_of_Trials=3
correct=False

for i in range(Number_of_Trials):
    try:
        player_input=int(input("Type your guess number "+str(i+1) + " "))
    except ValueError:
        print("Input must be an integer.")
        continue 
    if player_input<Target_number:
        print("Higher")
    elif player_input>Target_number:
        print("Lower")
    else:
        print("You're a genius, Congratulations")
        correct=True
        break
try:
    if correct==True:
        pass
    else:
        print("Sorry you have exhausted your trials")
except NameError:
    print("You didn't enter any valid input")

finally:
    print("Thank You for Playing")

