from tkinter import *

def selection():
    if (x.get() == 0):
        print("Healing!")
    elif (x.get() == 1):
        print("Slash!")
    elif(x.get() == 2):
        print("Sparkles!")

win = Tk()
characters = ["Priest", "Knight", "Mage"]
Priest = PhotoImage('images\Priest.png')
knigh = PhotoImage('images\Knight.png')
Mage = PhotoImage('images\Mage.png')

char_images = [Priest, knigh, Mage]


x = IntVar()

for i in range(len(characters)):
    radio_btn = Radiobutton(win, 
                            text = characters[i], ##adds text
                            variable=x, #groups radiobuttons togheter
                            value=i,
                            padx = 25,
                            image = char_images[i],
                            compound = 'left',
                            command=selection
                            ) #assigns a value to the radiobutton
    

    radio_btn.pack(side=LEFT)


win.mainloop()