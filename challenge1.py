""""""""
# challenge 001
firstname = input("Please enter your first name: ")
print ("Hello ", firstname)
""""""""

# challenge 002
firstname = input("Please enter your first name: ")
surname = input("please enter your surname: ")
print ("Hello ",firstname, surname)

# challenge 003
print ("what do you call a bear with no teeth?\nA gummy bear!")

# challenge 004
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
answer = num1 + num2
print ('The answer is ', answer)

# challenge 005 
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))
answer = (num1 + num2)* num3
print ('The answer is ', answer)

# challenge 006
startNum = int(input("Enter the number or slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
sliceLelf = startNum - endNum
print ("You have", sliceLelf, "slices remaining")

# challenge 007
name = input('what is your name? ')
age = int(input("How old are you? "))
newAge = age + 1
print (name, "next birthday you will be", newAge)

# challenge 008
bill = int(input("What is the total cost of the bill? "))
people = int(input('How many people are there? '))
each = bill/people 
print("Each person should pay $", each)

#challenge 009
days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In", days, "days there are ")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "secondes")

#challenge 010
kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is", pound, "pounds")

#challenge 011
larger = int(input("Enter the number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer =larger//smaller
print(smaller, "goes into", larger, answer, "times")
