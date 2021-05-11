# Snake || Water || Gun __ Game

import random

times = 10 # times to play game

comp_choice = ["s","w","g"] # output choice for computer

user_point = 0 # user point is initially marked 0
comp_point = 0 # computer point is initially marked 0


while times >= 1:
    comp_rand = random.choice(comp_choice) # output computer will give
    # 
    # print(comp_rand) # checking if the code is working or not

    print(f"ROUND LEFT = {times}")

# checking if the input is entered correct or not
    try:
        user_choice = input("Enter the input in lowercase ex. \n (snake- s) (water- w) (gun- w)\n:- ") # user choice, the user will input
    except Exception as e:
        print(e)

# if input doen't match this will run
    if user_choice != 's' and user_choice != 'w' and user_choice != 'g':
            print("Invalid input, try again\n")
            continue

# checking the input and calculating score
    if comp_rand == 's':
        if user_choice == 'w':
            comp_point += 1
        elif user_choice == 'g':
            user_point += 1
 
    elif comp_rand == 'w':
        if user_choice == 'g':
            comp_point += 1
        elif user_choice == 's':
            user_point += 1
 
    elif comp_rand == 'g':
        if user_choice == 's':
            comp_point += 1
        elif user_choice == 'w':
            user_point += 1
    
    times -=1 # reducing the number of rounds after each match

if user_point>comp_point: # if user wins
    print(f"WOOUUH! You have win \nYour_point = {user_point}\nComputer_point = {comp_point}")
elif comp_point>user_point: # if computer wins
    print(f"WE RESPECT YOUR HARD WORK, BUT YOU LOSE AND YOU ARE A LOSER NOW! \nYour_point = {user_point}\nComputer_point = {comp_point}")
elif comp_point==user_point: # if match draw
    print(f"MATCH DRAW\nYour_point = {user_point}\nComputer_point = {comp_point}")

else: # just checked 
    print("can't calculate score")

exit = input("PRESS ENTER TO EXIT")