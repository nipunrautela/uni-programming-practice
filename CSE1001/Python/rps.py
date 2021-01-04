import random

options = {"r": 1, "p": 2, "s": -1}
comp_s, player_s = 0, 0

while True:
    if comp_s == 10:
        print("Computer won!")
        break
    elif player_s == 10:
        print("You won!")
        break
        
    player = input("Choose: ")
    comp = random.choice(["r", "p", "s"])
    print(comp)
    if options[player]-options[comp] in [-1, 3, -2]:
        comp_s += 1
    elif options[player]-options[comp] in [1, -3, 2]:
        player_s += 1
    
    print("Score:", comp_s, "-", player_s)
