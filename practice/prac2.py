import random

computer = 0
player = 0

print("Welcome")

def choice():
    print("Player Turn :")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    ch = input("Enter Choice : ")

    switch = {
        "1":"Rock",
        "2":"Paper",
        "3":"Scissors"
    }

    return switch.get(ch,"Invalid!")

def comp_choice():
    r=random.randint(1,3)

    switch = {
        1:"Rock",
        2:"Paper",
        3:"Scissors"
    }

    return switch.get(r,"Invalid!")



def win(player_choice,computer_choice):
    global player,computer
    if player_choice == computer_choice:
        return "Tie"
    if (player_choice == "Rock" and computer_choice == "Scissors") or \
        (player_choice == "Paper" and computer_choice == "Rock") or \
        (player_choice == "Scissors" and computer_choice == "Paper") :
            player+=1
            return "Players Wins"
    elif (player_choice == "Scissors" and computer_choice == "Rock") or \
         (player_choice == "Rock" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Scissors") :
        computer += 1
        return "Computer Wins"
    else:
        return "Invalid "


while True:
    player_choice = choice()
    print("Player Choice : ",player_choice)
    computer_choice = comp_choice()
    print("Computer Choice : ",computer_choice)
    winner = win(player_choice,computer_choice)
    print(winner)
    print("\nScores :\nComputer : ",computer,"\nPlayer : ",player,"\n")
    if(computer == 3):
         print("Computer Won! ")
         break
    elif(player == 3):
         print("Player Won! ")
         break
         
        
        
