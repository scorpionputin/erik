#Kasutan Tkinter enda graafiliseks liideseks
from tkinter import *

aken = Tk()
aken.title("Pythoni töö")
aken.geometry("500x200")

count = 0

def nupp():
    global count
    count += 1
    if count == 1:
        print("Nupp vajutatud", count, "kord")
    else:
        print("Nupp vajutatud", count, "korda")


nupp = Button(aken, text="Sa võid seda nuppu vajutada, kui tahad.", command=nupp)
nupp.pack()

aken.mainloop()