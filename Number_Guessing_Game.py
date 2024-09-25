import random

def guess_a_number():
    """
        we need to ask an input to guess a number
        check to see if the number is too high or just right
        the can gues number 1 through 100
    """

    random_numb = random.randint(1, 100)
    while True:
        try:
            random_choice = int(input("Guess number between 1 and 100: "))

            if random_choice == random_numb:
                print("this is the number")
            elif random_choice > random_numb:
                print("To low!")
            elif random_choice < random_numb:
                print("To high!")
            else:
                print("BING BING BING! Right on the money.")
        except ValueError:
            print("Please enter a valid number")

guess_a_number()