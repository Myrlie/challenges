#challenge 052
import random
num = random.randint(1,100)
print(num)

#challenge 053
import random
fruit = random.choice(['apple', 'orange', 'grape', 'banana', 'strawberry'])
print(fruit)

#challenge 054
import random
coin = random.choice(["h", "t"])
guess = input("Enter (h)eads or (t)ails: ")
if guess == coin:
    print('You win')
else:
    print("Bad luck")
if coin == "h":
    print("It was heads")
else:
    print("It was tails")
    
#challenge 055
import random
num = random.randint(1,5)
guess = int(input("Enter a number: "))
if guess == num:
    print("Well done")
elif guess > num:
    print("Too high")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")
elif guess < num:
    print('Too low')
    guess =int(input("Guess again: "))
    if guess == num:
        print ("Correct")
    else:
        print("You lose")
        
#chalenge 056
import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
        
        
#challenge 057
import random
num = random.randint(1,10)
correct = False 
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
        
#challenge 058
import random
score = 0
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, "+", num2, "-")
    answer = int(input('Your answer: '))
    print()
    if answer == correct:
        score = score+1
print("You scored",score, "out of 5")

#challenge 059
import random
colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, while or pink")
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print("well done")
        tryagain = False
    else:
        if colour == "red":
            print("I bet you are seeing RED right now!")
        elif colour == "blue":
            print("Don't feel BLUE.")
        elif colour == "GREEN":
            print("I bet you are GREEN with envy right now.")
        elif colour == "White":
            print("Are you WHITE as a sheet, as you didn't guess correctly? ")
        elif colour == "pink":
            print("Shame you are not feeling in the PINK, as you got it wrong!")
    