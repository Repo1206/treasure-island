import time


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
time.sleep(2.5)
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
time.sleep(2.5)
print("You received a letter from a distant relative. The letter holds a map to a hidden treasure.")
time.sleep(2.5)
print("upon arriving to the island you are met by a fork in the road. Do you turn left or right? ")
time.sleep(2.5)
choice1 = input("Type Left or Right\n").lower()
if choice1 == "left":
  print("You turn left and come across a raging river. You dont know how to swim, but There is a log floating near by. You hear a low growl coming from behind a tree. Do you wait for the log to come closer? or attempt to swim away? ")
  choice2 =input("swim or wait? ")
  if choice2 == "wait":
    print("You jump to the log at the last possible second, avoiding the jaws of the angry beast behind you.")
    time.sleep(2.5)
    print("You hold on for dear life as the log is swept down stream.")
    time.sleep(2.5)
    print("all of a sudden, you notice the river is headed towards a massive waterfall.")
    time.sleep(2.5)
    print("You fight to steer the log away as the current drags you ever closer to your doom.")
    time.sleep(2.5)
    print("Left with little options, you leap back to the safety on the shore just as the log goes careening over the waterfall.")
    time.sleep(2.5)
    print("You pick yourself up, brush the dirt off and look up.")
    time.sleep(2.5)
    print("You now stand in front of three massive doors.")
    time.sleep(2.5)
    print("A red door with a Dragon embelm.")
    time.sleep(2.5)
    print("A yellow door with a Sun emblem.")
    time.sleep(2.5)
    print("And a blue door with the head of a Gryphon.")
    time.sleep(2.5)
    choice3 = input("Which door do you open? red, yellow, or blue? ")
    if choice3 == "yellow":
      print("You open the yellow door. A room filled with Golden treasures is your reward.\n You win!")
    elif choice3 == "red":
      print("You open the red door and are instantly burned by fire.\nGame over")
    elif choice3 == "blue":
      print("You open the blue door and a massive beast swallows you whole.\nGame over")
    else:
      print("Game over.")
  if choice2 == "swim":
    print("Attacked by trout.\nGame over")
elif choice1 == "right":
  print("Fall into a hole\nGame over")

