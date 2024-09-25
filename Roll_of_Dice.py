import random


def dice_roll():

   while True:
      roll_die_or_not =  input("do you want to roll the die? (y/n): ").lower()


      if roll_die_or_not == "y":
         first_die = random.randint(1, 6)
         second_die = random.randint(1, 6)
         print(f'({first_die}, {second_die})')
      elif roll_die_or_not == "n":
         print("Maybe next time")
         break
      else:
         print('Invalid Choice')





dice_roll()