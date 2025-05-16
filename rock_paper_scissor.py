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

win = '''


██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗          
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║          
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║          
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║          
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝╚═╝
                                                                
'''                              

loose = '''


██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗  ██████╗ ███████╗███████╗          
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔═══██╗██╔════╝██╔════╝          
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║██║   ██║███████╗█████╗            
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║██║   ██║╚════██║██╔══╝            
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝╚██████╔╝███████║███████╗    ██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝╚═╝
                                                                                   
'''

draw = '''



██████╗ ██████╗  █████╗ ██╗    ██╗          
██╔══██╗██╔══██╗██╔══██╗██║    ██║          
██║  ██║██████╔╝███████║██║ █╗ ██║          
██║  ██║██╔══██╗██╔══██║██║███╗██║          
██████╔╝██║  ██║██║  ██║╚███╔███╔╝    ██╗██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝     ╚═╝╚═╝
                                         
'''


import random

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("\nYou typed an invalid input. You loose!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"\nComputer chooses:\n{images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
      print(win)
    elif computer_choice > user_choice:
      print(loose)
    elif user_choice == 2 and computer_choice == 0:
      print(loose)
    elif user_choice > computer_choice:
      print(win)
    elif user_choice == computer_choice:
      print(draw)
