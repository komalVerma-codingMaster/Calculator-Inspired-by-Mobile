# Import Statements :-
from tkinter import PhotoImage, Tk, Button, Entry, Label
from tkinter.constants import FLAT

# Specific Variables :-
# Size/Co-ordinate Variables :-
rootWidth = 400
rootHeight = 600
buttonHeight_1 = int(rootHeight/10)
buttonWidth_1 = int(rootWidth/4)
buttonWidth_2 = int(rootWidth/2)
buttonPosY_1 = int(rootHeight-(buttonHeight_1*1))
buttonPosY_2 = int(rootHeight-(buttonHeight_1*2))
buttonPosY_3 = int(rootHeight-(buttonHeight_1*3))
buttonPosY_4 = int(rootHeight-(buttonHeight_1*4))
buttonPosY_5 = int(rootHeight-(buttonHeight_1*5))

# Color Scheme :-
white = "#ffffff"
black = "#000000"
orange = "#ecb251"

# For font :-
fontComb_1 = ("Open Sans", 20)
fontComb_2 = ("Open Sans", 28)

# Borderwidth Variables :-
borderWidth = 0.5

# Root Window :-
root = Tk()
root.title("Calculator (Inspired by Mobile)")
root.config(background=white)
# root.iconbitmap("C:/Users/Sunil Kumar/3D Objects/Coding Files/Software/Python/Calculator (Inspired by Mobile)/Media/icon.ico")
root.geometry("{}x{}".format(rootWidth, rootHeight))
root.minsize(rootWidth, rootHeight)
root.maxsize(rootWidth, rootHeight)

# All Functions :-
def changements_1(event):
     btn_divide["background"] = orange

# Main Content :-
# Importing Images :-
backspaceImg = PhotoImage("backspace.png")
mainBgImg = PhotoImage("mainBg.png")

# Main Background :-
mainBg = Label(root, image=mainBgImg, borderwidth=0, background=white)
mainBg.place(x=int((rootWidth/2)-100), y=25)

# Button - 0 :-
btn_0 = Button(root, text="0", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_0.place(x=0, y=buttonPosY_1, width=buttonWidth_2, height=buttonHeight_1)

# Button - Dot :-
btn_dot = Button(root, text=".", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_dot.place(x=0+(buttonWidth_1*2), y=buttonPosY_1, width=buttonWidth_1, height=buttonHeight_1)

# Button - EqualTo :-
btn_equalTo = Button(root, text="=", foreground=white, background=orange, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=orange, activeforeground=white)
btn_equalTo.place(x=0+(buttonWidth_1*3), y=buttonPosY_1, width=buttonWidth_1, height=buttonHeight_1)

# Button - 1 :-
btn_1 = Button(root, text="1", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_1.place(x=0, y=buttonPosY_2, width=buttonWidth_1, height=buttonHeight_1)

# Button - 2 :-
btn_2 = Button(root, text="2", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_2.place(x=0+(buttonWidth_1*1), y=buttonPosY_2, width=buttonWidth_1, height=buttonHeight_1)

# Button - 3 :-
btn_3 = Button(root, text="3", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_3.place(x=0+(buttonWidth_1*2), y=buttonPosY_2, width=buttonWidth_1, height=buttonHeight_1)

# Button - Plus :-
btn_plus = Button(root, text="+", foreground=white, background=orange, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=orange, activeforeground=white)
btn_plus.place(x=0+(buttonWidth_1*3), y=buttonPosY_2, width=buttonWidth_1, height=buttonHeight_1)

# Button - 4 :-
btn_4 = Button(root, text="4", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_4.place(x=0, y=buttonPosY_3, width=buttonWidth_1, height=buttonHeight_1)

# Button - 5 :-
btn_5 = Button(root, text="5", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_5.place(x=0+(buttonWidth_1*1), y=buttonPosY_3, width=buttonWidth_1, height=buttonHeight_1)

# Button - 6 :-
btn_6 = Button(root, text="6", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_6.place(x=0+(buttonWidth_1*2), y=buttonPosY_3, width=buttonWidth_1, height=buttonHeight_1)

# Button - minus :-
btn_minus = Button(root, text="-", foreground=white, background=orange, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=orange, activeforeground=white)
btn_minus.place(x=0+(buttonWidth_1*3), y=buttonPosY_3, width=buttonWidth_1, height=buttonHeight_1)

# Button - 7 :-
btn_7 = Button(root, text="7", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_7.place(x=0, y=buttonPosY_4, width=buttonWidth_1, height=buttonHeight_1)

# Button - 8 :-
btn_8 = Button(root, text="8", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_8.place(x=0+(buttonWidth_1*1), y=buttonPosY_4, width=buttonWidth_1, height=buttonHeight_1)

# Button - 9 :-
btn_9 = Button(root, text="9", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_9.place(x=0+(buttonWidth_1*2), y=buttonPosY_4, width=buttonWidth_1, height=buttonHeight_1)

# Button - Multiply :-
btn_multiply = Button(root, text="*", foreground=white, background=orange, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=orange, activeforeground=white)
btn_multiply.place(x=0+(buttonWidth_1*3), y=buttonPosY_4, width=buttonWidth_1, height=buttonHeight_1)

# Button - C :-
btn_C = Button(root, text="C", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_C.place(x=0, y=buttonPosY_5, width=buttonWidth_1, height=buttonHeight_1)

# Button - Null :-
btn_null = Button(root, text="÷", foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white, activeforeground=black)
btn_null.place(x=0+(buttonWidth_1*1), y=buttonPosY_5, width=buttonWidth_1, height=buttonHeight_1)

# Button - Backspace :-
btn_backspace = Button(root, image=backspaceImg, foreground=black, background=white, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=white)
btn_backspace.place(x=0+(buttonWidth_1*2), y=buttonPosY_5, width=buttonWidth_1, height=buttonHeight_1)

# Button - Divide :-
btn_divide = Button(root, text="÷", foreground=white, background=orange, font=fontComb_1, relief=FLAT, borderwidth=borderWidth, activebackground=orange, activeforeground=white)
btn_divide.place(x=0+(buttonWidth_1*3), y=buttonPosY_5, width=buttonWidth_1, height=buttonHeight_1)

# Entry Point :-
mainEntry = Entry(root, foreground=black, background=white, font=fontComb_2, relief=FLAT, borderwidth=0)
mainEntry.place(x=0+5, y=int(rootHeight-(buttonHeight_1*6)), width=rootWidth-10, height=buttonHeight_1)

# Exit Statements :-
root.mainloop()
