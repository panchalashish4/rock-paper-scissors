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


images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >= 3 or user < 0:
  print("You lose, Game Over!!!")
else:
  print(images[user])
  bot = random.randint(0,2)
  print(f"Computer Choose:\n{images[bot]}")

  if (user == bot):
    print("Draw")
  elif(user == 0 and bot == 1) or (user == 1 and bot == 2) or (user == 2 and bot == 0):
    print("You Lose")
  elif(user == 0 and bot == 2) or (user == 1 and bot == 0) or (user == 2 and bot == 1):
    print("You Win")
  else:
    print("invalid choice")


