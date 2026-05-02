from tkinter import *
from tkinter import ttk

#Everything about the window
wordle_window = Tk() #window instantion 
wordle_window.geometry("400x200")
wordle_window.title("Wordle Clone Type shii") # not useful for linux hyprland so cant test if this works proper

label = Label(wordle_window,text="wordle clone",font=('Satoshi',20,'bold'),fg='#00FF00')
label.pack()

#Run the window 
wordle_window.mainloop()
