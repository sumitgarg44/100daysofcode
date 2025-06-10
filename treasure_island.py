from static.arts import gameover, treasure

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.PURPLE + treasure.logo + color.END)

GAMEOVER = color.RED + gameover.logo + color.END

TREASURE = color.CYAN + treasure.richie_rich + color.END

print(color.BOLD + "Welcome to Treasure Island." + color.END)
print(color.BOLD + "Your mission is to find the treasure." + color.END) 

choice1 = input("\nYou are at cross road. Where do you want to go? Type Left or Right.\n").lower()

if choice1 == 'left':
  choice2 = input('\nYou came to a lake. There is an island in middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input('\nYou arrive at island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
    if choice3 == "red":
      print(GAMEOVER)
    elif choice3 == "blue":
      print(GAMEOVER)
    elif choice3 == "yellow":
      print(TREASURE)
    else:
      print(GAMEOVER)
  else:
    print(GAMEOVER)
else:
  print(GAMEOVER)
