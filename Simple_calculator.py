while True:
    option = input("Pick between Addition/Subtraction/Multiplication/Division or Q to quit: ").lower()

    if option == "q":
        quit()
    elif option == "addition" or option == "a":
        while True:
            first_number = (input("Enter first number: "))
            if first_number.isdigit():
                second_number = (input("Enter second number: "))
                if second_number.isdigit():
                    sum = int(first_number) + int(second_number)
                    print(sum)
                    break
            else:
                print("You must enter a digit")
                continue
    elif option == "subtraction" or option == "s":
        while True:
            first_number = input("Enter first number: ")
            if first_number.isdigit():
                second_number = input("Enter second number: ")
                if second_number.isdigit():
                    print(int(first_number) - int(second_number))
                    break
            else:
                print("You must enter a digit")
                continue
    elif option == "multiplication" or option == "m":
        while True:
            first_number = input("Enter first number: ")
            if first_number.isdigit():
                second_number = input("Enter second number: ")
                if second_number.isdigit():
                    print(int(first_number) * int(second_number))
                    break
            else:
                print("You must enter a digit")
                continue
    elif option == "division" or option == "d":
        while True:
            first_number = input("Enter first number: ")
            if first_number.isdigit():
                second_number = input("Enter second number: ")
                if second_number.isdigit():
                    print(int(first_number) / int(second_number))
                    break
            else:
                print("You must enter a digit")
                continue
    else:
        print("Invalid Option")
        continue