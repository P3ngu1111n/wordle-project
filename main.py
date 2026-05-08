from tkinter import *
from tkinter import ttk



#Everything about the window
wordle_window = Tk() #window instantion 
wordle_window.geometry("400x200")


#user input 
user_input = Entry()
user_input.config(font=("sans-serif"),)
user_input.pack()



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



def submit() :
    user_guess = user_input.get()
    print (user_guess)


#buttons 
check_button = Button(
wordle_window,
text="check",
font=('Roboto',10),
pady=2 ,
command = submit, # a function call back goes in here 
)
check_button.pack()




#Run the window 
wordle_window.mainloop()



