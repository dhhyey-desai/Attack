import random
func = "yes", "y"
option=str(input("Hello there, would you like to play this game. Y/N\n"))
if option == str("Y"):
    print("Ok")
elif option == str("y"):
    print("Ok")
else:
    exit()
playerhp = 300
enemyatkl = -10
enemyatkh = 15
strikes = 0

while playerhp > 0:
    choice=int(input("Please select a number from 1-9\n"))
    if strikes > 10:
        enemyatkl = 5
        enemyatkh = 50
    choice = (choice % 9)+1
    dmg = random.randrange(enemyatkl, enemyatkh) * choice
    playerhp = playerhp - dmg

    strikes = strikes + 1
    if playerhp > 0:
        print("Enemy strikes for", dmg, "points. Current hp is", playerhp)
else:
    print("You have died, you survived for", strikes - 1, "strikes")







