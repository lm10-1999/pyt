print("Welcome to the quiz game")
playing = input("Do you wanna play? ")

if playing.lower() == "no":
    quit
print("let's play the game!!")
score=0

answer = input("Current Football World Cup winner? ")
if answer.lower() == ("france" or "France") :
    print("Correct answer")
    score+=1
else:
    print("Incorrect !")
    
answer = input("Tallest mountain in the world is? ")
if answer.lower()  == "mount everest"  :
    print("Correct answer")
    score+=1
else:
    print("Incorrect !")
    
answer = input("Closest planet to the sun is? ")
if answer.lower() == "mercury" :
    print("Correct answer")
    score+=1
else:
    print("Incorrect !")
    
answer = input("What does RAM stand for? ")
if answer.lower()  == ("random access memory") :
    print("Correct answer")
    score+=1
else:
    print("Incorrect !")
    
print("You got " + str(score) + " questions correct")