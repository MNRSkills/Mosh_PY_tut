import random


def rock_paper_scissors():
    """
    My attempt at this solution is first commit
        we first need to generate random R/P/S
        Then we need to ask te user to choose


    Second commit will be Moshs version
    """
    machine = random.choice(["rock", "paper", "scissor"])
    print(machine)
    while True:
            try:
                pick_item = input("Rock, Paper, or Scissors? (rock/paper/scissor)").lower()
                if pick_item == machine:
                    print("Tie!")
                elif pick_item != machine:
                    print(f'User picked {pick_item} and the machine picked {machine}')
                break
            except ValueError:
                print("THIS IS DOING SOMETHING")

rock_paper_scissors()