from tkinter import *
from datetime import date
root = Tk()
root.title("Getting started with widgets")
root.geometry("1200x900")
lbl = Label(text="Hey there!",fg="white",bg="#C1E4E4",height="1",width="300")
name_lbl = Label(text="Full name",bg="#59CE98")
name_entry = Entry()
def Display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! \nToday's date is:"
    greet = "Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height=3)
btn = Button(text="Begin", command=Display, height=1, bg="#1DE11D")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()