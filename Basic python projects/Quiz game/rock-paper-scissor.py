import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]
while True:
    user_input = (input("Type rock/paper/scissors or Q to quit : ")).lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Not a valid string")
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("User wins")
        user_wins+=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("User wins")
        user_wins+=1
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("User wins")
        user_wins+=1
        
    else:
        print("You lost!")
        computer_wins+=1
        
print("You won",user_wins,"time(s)")
print("Computer wins",computer_wins,"time(s)")

print("F off")
    
    
    