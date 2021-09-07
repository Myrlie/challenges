#challenge 045
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num 
    print("The total is ", total)
    
#challenge 046
num = 0 
while num <= 5:
    num = int(input("Enter a number: "))
print('The last number you enterd was a', num)

#challenge 047
num1 = int(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
    num2= int(input("Enter another number: "))
    total = total + num2
    again = input("Do you want to add another number? (y/n)")
    print("The total is ", total)
    
#challenge 048
again = "Y"
count = 0 
while again =='Y':
    name = input("Enter a name of somebody you want to invite to your party: ")
    print(name, "has now been invited")
    count = count + 1
    again = input("Do you want to invite somebody else? (y/n) ")
print("You have", count, "people coming to your party")

#challenge 049
compnum = 50
guess = int (input("Can you guess the number I am thinking of? "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else:
        print ("Too high")
    count = count+1
    guess = int(input ("Have you another guess: "))
print("Well done, you look", count, "attempts")

#challenge 050
num = int(input("Enter a number between 10 and 20: "))
while num <10 or num >20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again: "))
print("Thank you")

#challenge 051
num = 10
while num>0:
    print ("There are ", num, "green bottle on wall.")
    print(num, "green bottles hanging on the wall,")
    print("And if 1 green bottle shoud accidentally fall.")
    answer = int(input("How many green bottles hanging on the wall? "))
    if answer == num :
        print ("There will be", num, "green bottles hanging on the wall.")
    else:
        while answer !=num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall")    