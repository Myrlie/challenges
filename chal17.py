133

from tkinter import *

def click ():
    name = textbox1.get() 
    message = str("Hello " + name)
    textbox2["text"] = message

window = Tk ()
window.title ("Names"). window.geometry ("450x350")
window.wm_iconbitmap ("stripes.ico")
window.configure (background= "black")

logo = PhotoImage (file = "Mylogo.gif") 
logoimage= Label (image = logo) 
logoimage.place (x = 100, y=20, width = 200,  height = 150)

label1 = Label (text = "Enter your name:")
label1.place(x = 30, y=200) 
label1["bg"] = "black"
label1["fg"]= "white"

textbox1 =Entry (text = "") 
textbox1.place (x = 150, y = 200,width=200, height=25) 
textbox1["justify"] = "center"
textbox1.focus ()

button1 = Button (text="Presa me", command = click) 
button1.place (x = 30, y=250, width = 120, height = 25)
button1 ["bg"] = "yellow"

textbox2 = Message (text = "") 
textbox2.place (x=150, y=250, width=200, height=25)
textbox2 ["bg"] = "white" 
textbox2 ["fg"] = "black"

#challenge 134

from tkinter import *
import random

def checkans ():
    theirans = ansbox.get() 
    theirans = int(theirans)
    num1 = num1box["text"] 
    num1 = int(num1)
    num2 = num2box["text"]
    num2 = int(num2)
    ans = num1 + num2 
    if theirans == ans:
        img = PhotoImage (file = "correct.gif") 
        imgbx.image = img
    else:
        img = PhotoImage (file = "wrong.gif") 
        imgbx.image = img
    imgbx["image"]= img
    imgbx.update()

def nextquestion (): 
    ansbox.delete (0, END)
    num1 = random.randint (10,50)
    num1box["text"] = num1
    num2 = random.randint (10,50)
    num2box["text"] = num2
    img = PhotoImage (file = "")
    imgbx.image = img
    imgbx ["image"]=img 
    imgbx.update()

window = Tk ()
window.title = ("Addition") 
window.geometry ("250x300")

num1box = Label (text = "0")
num1box.place (x = 50, y = 30, width = 25 , height=25)
addsymbl = Message (text = "") 
addsymbl.place (x = 75, y = 30, width = 25, height=25) 
num2box = Label (text = "0")
num2box.place (x = 100, y = 30, width = 25, height=25) 
eqlsymbl = Message (text = "=" )
eqlsymbl.place(x = 125, y = 30, width = 25, height = 25) 
ansbox = Entry (text = "")
ansbox.place (x = 150, y=30, width = 25, height = 25)
ansbox ["justify"]="center"
ansbox.focus() 
checkbtn = Button (text = "Check", command = checkans)
checkbtn.place (x = 50, y = 60, width = 75, height = 25)
nextbtn = Button (text = "Next", command = nextquestion) 
nextbtn.place (x = 130, y = 60, width= 75, height = 25)
img = PhotoImage (file = "")
imgbx = Label(image = img) 
imgbx.image = img
imgbx.place (x=25, y = 100, width = 200, height=150)

nextquestion ()

window.mainloop()

#challenge 135

from tkinter import *

def clicked ():
    sel = selectcolour.get ()
    window.configure (background = sel)

window = Tk
window.title ("background") 
window.geometry("200x200")

selectcolour = StringVar(window)
selectcolour.set ("Grey")

colourlist = OptionMenu(window, selectcolour, "Grey","Red", "a1","Green", "Yellow")
colourlist.place (x = 50 , y = 30)

clickme = Button (text= "Click Me", command =clicked)
clickme.place ( x = 50 , y = 150, width = 60, height = 30)

mainloop()

#challenge 136

from tkinter import *

def add_to_list ():
    name = namebox.get() 
    namebox.delete (0, END)
    genderselection = gender.get() 
    gender.set ("M/F")
    newdata = name + ", " + genderselection + "\n" 
    name_list.insert (END, newdata) 
    namebox.focus ()

window = Tk ()
window.title ("People List") 
window.geometry ("400x400")

namelbl= Label (text = "Enter their name:")
namelbl.place (x = 50, y = 50, width= 100, height=25) 
namebox = Entry (text = "") 
namebox.place (x = 150, y = 50 , width = 150,  height = 25)
namebox.focus ()

genderlbl = Label (text = "Select Gender") 
genderlbl.place ( x = 50, y = 100 , width = 100, height = 25) 
gender = StringVar (window)
gender.set ("M/F")
gendermenu = OptionMenu (window, gender, "M", "F")
gendermenu.place (x = 150, y = 100)

name_list = Listbox ()
name_list.place( x = 150 , y = 150, width = 150 , height=100) 
addbtn = Button (text ="Add to List", command = add_to_list) 
addbtn.place (x = 50, y = 300, width=100, height = 25)

window.mainloop()

#challenge 137

from tkinter import *

def add_to_list ():
    name = namebox.get() 
    namebox.delete (0, END)
    genderselection = gender.get() 
    gender.set ("M/F")
    newdata = name + ", " + genderselection + "\n"
    name_list.insert (END, newdata)
    namebox.focus ()
    file = open("names.txt", "a")
    file.write (newdata)
    file.close()

def print_list():
    file = open("names.txt","r")
    print (file.read())

window = Tk()
window.title ("People List") 
window.geometry ("400x400")

namelbl = Label (text = "Enter their name:")
namelbl.place(x = 50, y = 50, width= 100, height=25)
namebox = Entry (text = "")
namebox.place (x = 150, y = 50, width=150, height=25) 
namebox.focus()

genderlb1 = Label (text= "Select Gender")
genderlbl.place (x = 50, y = 100, width=100, height=25)
gender = StringVar (window) 
gender.set ("M/F")
gendermenu = OptionMenu (window, gender, "M","F")
gendermenu.place ( x=150, y = 100)

name_list = Listbox ()
name_list.place (x = 150, y = 150, width = 150, height=100)

addbtn = Button (text = "Add to List", command = add_to_list) 
addbtn.place(x = 50, y = 300 , width=100, height = 25)

printlst = Button (text = "Print List", command= print_list)
printlst.place (x = 175, y = 300, width = 100, height=25)

window.mainloop()

#challenge 138

from tkinter import *

def clicked ():
    num = selection.get() 
    artref = num + ".gif"
    photo = PhotoImage (file = artref) 
    photobox.image = photo 
    photobox ["image"]=photo
    photobox.update ()

window = Tk ()
window.title ("Art") 
window.geometry("400x350")

art = PhotoImage (file="1.gif")
photobox = Label (window, image = art)
photobox.image = art
photobox.place ( x = 100, y = 20 , width=200, height=150)

label = Label (text = "Select Art number: ")

label.place ( x = 50 , y = 200, width = 100, height =25)

selection = Entry (text = "") 
selection.place ( epsilon = 200, y = 200, width=100,height=25) 
selection.focus ()

button = Button (text = "See Art", command = clicked) 
button.place (x = 150, y=250, width=100, height =25)

window.mainloop()