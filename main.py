import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)
else:
    print("invalid option")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(rock)
    print("Computer's choice is Rock")
elif computer_choice == 1:
    print(paper)
    print("Computer's choice is Paper")
elif computer_choice == 2:
    print(scissors)
    print("Computer's choice is Scissors")

if your_choice == 0 and computer_choice == 2:
  print("You win")
elif your_choice == 0 and computer_choice == 1:
  print("You lose")
elif your_choice == 0 and computer_choice == 0:
  print("Draw")

if your_choice == 1 and computer_choice == 0:
  print("You win")
elif your_choice == 1 and computer_choice == 2:
  print("You lose")
elif your_choice == 1 and computer_choice == 1:
  print("Draw")

if your_choice == 2 and computer_choice == 0:
  print("You win")
elif your_choice == 2 and computer_choice == 1:
  print("You lose")
elif your_choice == 2 and computer_choice == 2:
  print("Draw")
