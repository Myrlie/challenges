# challenge 080
fname = input("Enter your first name: ")
print("That has", len(fname), "characters in it")
sname = input("Enter your surname: ")
print("That has", len(sname), "characters in it")
name = fname + " " + sname
print("Your full name is", name)
print("That has", len(name), "characters in it")

#challenge 081
subject = input("Enter your favourite school subject: ")
for letter in subject:
    print(letter, end = "-")
    
#challenge 082
poem = "Oh, I wish I'd looked after me teeth, "
print (poem)
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
print(poem[start:end])

#challenge 083
msg = input("Enter a message in uppercase: ")
tryagain = False
while tryagain == False:
    if msg.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again")
        msg = input("Enter a message in uppercase: ")
        
#challenge 084
postcode = input("Enter your postcode: ")
start = postcode[0:2]
print(start.upper())

#challenge 085
name = input("Enter your name: ")
count = 0
name = name.lower()
for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count = count + 1
print("Vowels =", count)

#challenge 086
pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")
if pswd1 == pswd2:
    print("Thank you")
elif pswd1.lower() == pswd2.lower():
    print("They must be the same case")
else:
    print("Incorrect")
    
#challenge 087
word = input("Enter a word: ")
length = len(word)
num = 1 
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
