import random
user_guesses = 1
random_number = random.randint(1, 10)

while True:
    user_guess = input("Type a number between 1-10 or Q to quit: ").lower()

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if 1 <= user_guess <= 10:
            
            if user_guess == random_number:
                print("Congrats")
                print("You guessed", user_guesses, "times")
                user_guesses = 1
                continue
            elif user_guess > random_number:
                print("The random number is lower")
                user_guesses += 1
                continue
            elif user_guess < random_number:
                print("The random number is higher")
                user_guesses += 1
                continue
        else:
            print("Please enter a number between 1-10")
            continue
    elif user_guess == "q":
        print("Quitting")
        break
    else:
        print("Please enter a digit")
        continue