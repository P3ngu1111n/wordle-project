from tkinter import *
from tkinter import ttk

#Everything about the window
wordle_window = Tk() #window instantion 
wordle_window.geometry("400x200")
wordle_window.title("Wordle Clone Type shii") # not useful for linux hyprland so cant test if this works proper

#wordle title
wordle_header = Label(
wordle_window,
text="Wordle Clone",
font=('Satoshi',20,'bold'),
fg='#00FF00',
# relief=RAISED, #border type 
# bd=10, #border thiccness
)
wordle_header.pack()

#buttons 
check_button = Button(
wordle_window,
text="check",
font=('Roboto',10),
pady=2 ,
# command= , # a function call back goes in here 
)
check_button.pack()

#user input 
user_guess = Entry()
user_guess.config(font=("sans-serif"),)
user_guess.pack()


#Run the window 
wordle_window.mainloop()
