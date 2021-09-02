#challenge 012
num1 =int(input("Enter first number "))
num2 =int(input("Enter second number "))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
    
#challenge 013
num = int(input("Enter a value less than 20: "))
if num >= 20:
    print("Too high")
else:
    print("Thank you")
    
#challenge 014
num = int(input("Enter a value between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

#challenge 015
colour = input("Type in your favorite colour: ")
if colour == 'red' or colour == 'RED' or colour == 'Red':
    print('I like red too.')
else:
    print("I don\'t like that colour, I prefer red")
    
#challenge 016
raining = input("Is it raining? ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umberella")
    else:
        print("Take an umberella")
else:
    print("Enjoy your day")
    
#challenge 017 
age = int(input("what is your age"))
if age >= 10:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print ("You can buy a lottery ticket")
else:
    print("You can go trick-or-Treating")
    
#challenge 018
num = int(input("Enter a number: "))
if num <10:
    print("Too low")
elif num >=10 and num<=20:
    print("Correct")
else:
    print("Too high")
    
#challenge 019
num = input("Enter 1, 2 0r 3")
if num =="1":
    print ("Thank you")
elif num == "2":
    print("well done")
elif num == "3":
    print("correct")
else:
    print("Error message")