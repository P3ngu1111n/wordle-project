from tkinter import *
from tkinter import ttk
from wonderwords import RandomWord
import tkinter as tk



#Window creation
root = Tk() #window instantion 
root.geometry("400x200")



#wordle title (Label)
wordle_header = Label(
root,
text="Wordle Clone",
font=('Satoshi',20,'bold'),
fg='#00FF00',
# relief=RAISED, #border type 
# bd=10, #border thiccness
)
wordle_header.pack()

#string var 
string_var = tk.StringVar()

#frames
frame_1 = tk.Frame(root)
frame_1.pack()

#user input(entry)
user_input_1 = Entry(frame_1, textvariable=string_var, width=1)
user_input_1.config(font=("sans-serif"),)

user_input_2 = Entry(frame_1, textvariable=string_var, width=1)
user_input_2.config(font=("sans-serif"),)

user_input_3 = Entry(frame_1, textvariable=string_var, width=1)
user_input_3.config(font=("sans-serif"),)

user_input_4 = Entry(frame_1, textvariable=string_var, width=1)
user_input_4.config(font=("sans-serif"),)

user_input_5 = Entry(frame_1, textvariable=string_var, width=1)
user_input_5.config(font=("sans-serif"),)


user_input_1.pack(side="left", padx=10, pady=10, ipadx=2)
user_input_2.pack(side="left", padx=10, pady=10, ipadx=2)
user_input_3.pack(side="left", padx=10, pady=10, ipadx=2)
user_input_4.pack(side="left", padx=10, pady=10, ipadx=2)
user_input_5.pack(side="left", padx=10, pady=10, ipadx=2)

#Num_Limit_warning(Label)


#Word_regenertion (Function)[Linked to the gnrt_button]
def regnrt() :
    r = RandomWord()
    rword =  r.word(word_min_length=5, word_max_length=5 )
    print (rword)
    return rword


#the check button (Function)[Linked to the check_button]
def submit() :
    user_guess = user_input.get()
    print (user_guess)
    return user_guess



#buttons 
check_button = Button(
root,
text="check",
font=('Roboto',10),
pady=2 ,
command = submit, # a function call back goes in here 
)


gnrt_button = Button(
    text="regenerate",
    font=('Roboto',10),
    pady=2 ,
    command = regnrt, 
)

check_button.pack()
gnrt_button.pack()

#Run the window 
root.mainloop()



