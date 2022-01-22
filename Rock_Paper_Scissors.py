import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]
while True:
    user_choice = input("Pick Rock, Paper, Scissor or Q to quit: ").lower()
    if user_choice == "q":
        if user_wins or computer_wins == 1:
            if user_wins and computer_wins == 1:
                print("You got", user_wins, "point")
                print("Computer got", computer_wins, "point")
                quit()
            if user_wins == 1:
                print("You got", user_wins, "point")
                print("Computer got", computer_wins, "points")
                quit()
            elif computer_wins == 1:
                print("You got", user_wins, "points")
                print("Computer got", computer_wins, "point")
                quit()
        else:
            quit()

    if user_choice not in options:
        print("Invalid option")
        continue

    random_number = random.randint(0, 2)
    #Rock 0, Paper 1, Scissor 2
    computer_choice = options[random_number]

    if user_choice == computer_choice:
        print("Tie")
        continue  
    elif user_choice == "rock" and computer_choice == "scissor":
        print("You got a point")
        user_wins += 1
        continue

    elif user_choice == "scissor" and computer_choice == "paper":
        print("You got a point")
        user_wins += 1       
        continue

    elif user_choice == "paper" and computer_choice == "rock":
        print("You got a point")
        user_wins += 1
        continue

    else:
        print("Computer got a point")
        computer_wins += 1
        continue
