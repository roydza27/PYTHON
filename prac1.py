import random

def roll():
    min_V = 1
    max_V = 6
    roll = random.randint(min_V,max_V)
    return roll

while True:
    players = input("Enter No. Of Players between (2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4 :
            break
        else:
            print("Enter Players Between (2 - 4)")
    else:
        print("Invalid Number! ")
        break

max_score = 50
players_lst = [0 for _ in range(players)]

while max(players_lst) < max_score:
    for k in range(players):
        print("\nPlayer ",k + 1," turn has Just Started!\n")

        cur_score = 0
        while True:
            should_roll = input("Would you like to roll (y/n) : ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You Rolled 1! Turn Done\n")
                cur_score = 0
                break
            else:
                cur_score+=value
                print("You Rolled a : ",value,"\n")
        players_lst[k] += cur_score 
        print("Your Current Score : ",players_lst[k])

max_score=max(players_lst)
winner = players_lst.index(max_score)
print("\nPlayer Number ",winner+1," has Won!\n"
      "His Score : ",max_score,"\n")
