import random

print("Welcome to the game!")

top_number = input("Type a number : ")
if top_number.isdigit():
    top_number = int(top_number)
    
    if top_number <= 0:
        print("Print mumber greater than 0")
        quit()
else:
    print("Print a valid digit")
    quit()

rand_no = random.randrange(0,top_number)
guesses =0

while True:
    guesses+=1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Print type a valid digit")
        continue
    
    if(user_guess == rand_no):
        print("Got itt!")
        break
    else:
        if(user_guess>rand_no):
            print("You were above the number")
        else:
            print("You were below the random number")
        
print("You got it in ",guesses,"guess(es)")