#challenge 096
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

#challenge 097
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
col = int(input("Select a column: "))
print(list[row] [col])

#challenge 098
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
print(list[row])
newvalue = int(input("Enter a new number: "))
list[row].append(newvalue)
print(list[row])

#challenge 099
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Select a row: "))
print(list[row])
col = int(input("Select a column: "))
print(list[row] [col])
change = input("Do you want to change the value? y/n ")
if change == "y":
    newvalue = int(input("Enter new value: "))
    list[row] [col] = newvalue
print(list[row])

#challenge 100
sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

#challenge 101
sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}
person = input("Enter sales person's name")
region = input("Select region: ")
print(sales[person][region])
newdata = int(input("Enter new data: "))
sales[person] [region] = newdata
print(sales[person])

#challenge 102
list = []
for i in range (0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age"))
    shoe = int(input("Enter shoe size: "))
    list[name]= {"Age":age,  "Shoe size":shoe}
    
ask = input("Enter a name: ")
print(list[ask])

#challenge 103
list = []
for i in range (0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age"))
    shoe = int(input("Enter shoe size: "))
    list[name]= {"Age":age,  "Shoe size":shoe}
    
for name in list:
    print((name), list[name] ["Age"])
    

#challenge 104
list = []
for i in range (0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age"))
    shoe = int(input("Enter shoe size: "))
    list[name]= {"Age":age,  "Shoe size":shoe}  
getrid = input("Who do you want to remove from the list? ")
del list[getrid]
for name in list:
    print((name), list[name] ["Age"],list[name] ["Shoe size"])

