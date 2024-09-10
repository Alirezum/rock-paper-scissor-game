from random import randint
import time

print(
    "Winning rules of the game ROCK PAPER SCISSORS are :\n"
    + "Rock vs Paper -> Paper wins\n"
    + "Rock vs Scissors -> Rock wins\n"
    + "Paper vs Scissors -> Scissors wins\n"
)

time.sleep(2)

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n")

    time.sleep(2)
    choice = int(input("Enter your choice:"))

    time.sleep(2)
    while choice > 3 or choice < 1:
        choice = int(input("Enter A valid choice:"))

    time.sleep(2)
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"

    print("User choice is :", choice_name)
    print("Now its Computer Turn...")

    time.sleep(2)
    pc_choice = randint(1, 3)

    if pc_choice == 1:
        pc_choice_name = "Rock"
    elif pc_choice == 2:
        pc_choice_name = "Paper"
    elif pc_choice == 3:
        pc_choice_name = "Scissors"

    time.sleep(2)
    print("Computer Choice is:", pc_choice_name)
    print(choice_name, "vs", pc_choice_name)

    time.sleep(2)
    if choice == pc_choice:
        result = "Draw"
    elif (choice == 1 and pc_choice == 2) or (pc_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and pc_choice == 3) or (pc_choice == 1 and choice == 3):
        result = "Rock"
    elif (choice == 2 and pc_choice == 3) or (pc_choice == 2 and choice == 3):
        result = "Scissors"

    time.sleep(2)
    if result == "Draw":
        print("<== It's a Tie ==>")
    elif result == choice_name:
        print("<== User Win ==>")
    else:
        print("<== Computer Win ==>")

    time.sleep(2)
    print("Do you want play Again?(Y/N): ")
    ansewr = input().lower()
    if ansewr == "n":
        break

print("Thanks for playing")

time.sleep(3)
