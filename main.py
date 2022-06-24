from tkinter import *
from time import strftime

root = Tk()
root.title("digital clock")
root.geometry("420x90")
root.configure(bg='yellow')
text = ("Boulder", 20, "bold")

label = Label(root, font=text)
label.pack(anchor="center")

def time():
    livetime = strftime("%H:%M:%S       %Z")
    label.config(text=livetime)
    label.after(1000, time)

time()

mainloop()
