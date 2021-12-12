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

autogen = [rock,paper,scissors]

print("Rock Paper Scissor Showdown!\n")

me = int(input("What do you choose?\n\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if me > 2 or me < 0:
    print("Oops! Did you type wrong?\n")
else:
  print(autogen[me])

  print("Computer choose:\n")

  cpugen = random.randint(0,2)
  print(autogen[cpugen])
  cpu = cpugen
  
  if me == 0 and cpu == 2:
    print("You Win!\n")
  elif cpu == 1 and me == 0:
    print("You lost!\n")
  elif cpu > me:
    print("You lose!\n")
  elif me > cpu:
    print("You win!\n")
  elif me == cpu:
    print("Draw!\n")

  print("Thanks for playing!\n")