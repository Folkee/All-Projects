while True:
    user_choice = input("Do you want to to go on an adventure type Yes or No: ").lower()
    if user_choice == "yes":
        while True:
            first_choice = input("You come to a crossroad you can go left or right type left or right: ").lower()
            if first_choice == "left":
                while True:
                    left_choice = input("The road ends and there is just forest everywhere do you turn back or try to go forward type back to turn back or forward to continue: ").lower()
                    if left_choice == "back":
                        print("On your way back you come across a bear and he attacks you and you die")
                        print("You lose!")
                        quit()
                    elif left_choice == "forward":
                        print("You come across a river and try to swim across and get eaten by an alligator")
                        print("You lose!")
                        quit()
                    else:
                        print("You need to enter either back or forward")
                        continue
            elif first_choice == "right":
                while True:
                    right_choice = input("You come to a abandoned house do you enter or pass and continue: ").lower()
                    if right_choice == "enter":
                        print("You enter the house and right after you enter the floor under you breaks and you die by spike traps under the floor")
                        print("You lose!")
                        quit()
                    elif right_choice == "continue":
                        print("You go around the house and continue and you find the city of light which was what you hoped to find")
                        print("You win")
                        quit()
                    else:
                        print("You need to enter either enter or continue")
                        continue
            else:
                print("You need to enter either left or right")
                continue
    elif user_choice == "no":
        quit()
    else:
        print("You need to enter either Yes or No")