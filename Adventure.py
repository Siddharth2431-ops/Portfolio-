print("You wake up in a dark forest")
choice = input("Do you go left or right?")
if choice.lower() == "left":
      print("You stumble upon a cave")
      print("Will you go in cave??")
yn = input("Yes or no?: ")
if yn.lower() == "yes":
      print("You have to fight with zombies, skeltons and creepers.")
if yn.lower() == "no":
      print("Then you have to move forward")
else choice.lower() == "right":
      print("You have found the exit portal.")