#challenge 111
import csv

file = open("Books.csv","w")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fritzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newrecord))
file.close()

#challenge 112
import csv
file = open("Books.csv","a")
title = input("Enter a title: ")
author = input("Enter author: ")
year = input("Enter the year it was released: ")
newrecord = title + "," + author + "," + year + "\n"
file.write(str(newrecord))
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()

#challenge 113
import csv
num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv","a")
for x in range (0, num):
    title = input("Enter a title: ")
    author = input("Enter author: ")
    year = input("Enter the year it was released: ")
    newrecord = title + "," + author + "," + year + "\n"
    file.write(str(newrecord))
file.close()

searchauthor = input("Enter an authors name to search for: ")

file = open("Books.csv","r")
count = 0
for row in file:
    if searchauthor in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There are no books by that author in this list.")
file.close()

#challenge 114
import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
    
x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <=end:
        print(tmp[x])
    x = x+1
    
#challenge 115
import csv

file = open("Books.csv","r")
x = 0
for row in file:
    display = "Row " + str(x) + " - " + row
    print(display)
    x = x + 1
    
#challenge 116
import csv

file = list(csv.reader(open("Books.csv")))
Booklist = []
for row in file:
    Booklist.append(row)
    
x = 0
for row in Booklist:
    display = x,Booklist[x]
    print(display)
    x = x + 1
getrid = int(input("Enter a row number to delete: "))
del Booklist[getrid]

x = 0
for row in Booklist:
    display = x,Booklist[x]
    print(display)
    x = x + 1
alter = int(input("Enter a row number to alter: "))
x = 0
for row in Booklist[alter]:
    display = x, Booklist[alter][x]
    print(display)
    x = x + 1
part = int(input("which part do you want to change? "))
newdata = input("Enter new data: ")
Booklist[alter][part] = newdata
print(Booklist[alter])

file = open("Books.csv", "w")
x = 0
for row in Booklist:
    newrecord = Booklist[x][0]+ ", " + Booklist[x][1]+ ", " + Booklist[x][2] + "\n"
    file.write(newrecord)
    x = x+1
file.close()

#challenge 117
import csv
import random

score = 0
name = input("What is your name: ")
q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)
question1 = str(q1_num1) + "+" + str(q1_num2) + "_"
ans1 = int(input(question1))
realans1 = q1_num2 + q1_num2
if ans1 == realans1:
    score = score + 1 
q2_num1 = random.randint(10,50)
q2_num2 = random.randint(10,50)
question2 = str(q2_num1) + "+" + str(q2_num2) + "_"
ans2 = int(input(question2))
realans2 = q2_num2 + q2_num2
if ans2 == realans2:
    score = score + 1 

file = open("QuizScore.csv", "a")
newrecord = name + ","+ question1 + "," + question2 + "," + str(ans2) + str(score)+"\n"
file.write(str(newrecord))
file.close()