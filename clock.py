import tkinter as tk
from time import strftime

root =tk.Tk()
root.title("DIGITSL CLOCK")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root,font=('calibri',80,'bold'),background='green',foreground='red')
label.pack(anchor='center')

time()

root.mainloop()