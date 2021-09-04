#challenge 027
num = float(input("Enter a number with lots of decimal places: "))
print(num*2)

#challenge 028
num = float(input("Enter a number with lots of decimal places: "))
answer = num*2
print(answer)
print (round(answer, 2))

#challenge 029
import math
num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print (round(answer, 2))

#challenge 030
import math
print(round(math.pi,5))

#challenge 031
import math
radius = int(input("Enter the radius of the circle: "))
area = math.pi*(radius**2)
print (area)

#challenge 032
import math
radius = int(input("Enter the radius of the circle: "))
depth = int(input('Enter depth: '))
area = math.pi*(radius**2)
volume = area*depth
print(round(volume, 3))

#challenge 033
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
ans1 = num1//num2
ans2 = num1%num2
print(num1, "divided by", num2, "is",  ans1, "with", ans2, "remaining.")

#challenge 034
print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the length of one side: "))
    area = side *side
    print("The area of your chosen shape is", area)
elif menuselection == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base*height)/2
    print("The area of your chosen shape is", area)
else:
    print("incorrect option selected")