# Tkinter

from tkinter import *
# importing all libraries of Tkinter

count=0

def clickFunc():
    print("Have a nice day")
    global count
    count+=1
    print("Count=",count)
    
windowNew=Tk()
# create a window named windowNew

windowNew.geometry("100x100")
# defining size of window in terms of height and width

windowNew.title("Label Window")
# renaming window 

logo=PhotoImage(file="Aesthetic.png")
windowNew.iconphoto(True,logo)
# renaming window 

windowNew.config(background="Royal Blue")
# config window allows to make changes to window
# changing color of window to royal blue
 
buttonNew= Button(
		       windowNew,text="Click Me",    # printing   text on GUI screen
		       command=clickFunc,
		       font=('Arial',50,'bold'),     # font for   text on GUI screen
		       fg='Orange',                  # font color text on GUI screen
		       bg='black',                   # background color text on GUI screen
		       activeforeground='Orange',    # font color text on GUI screen when button clicked
		       activebackground='black',     # background color text on GUI screen when button clicked
		       relief=RAISED,
		       bd=10,                        # border scale
		       padx=20,                      # space b/w  text  and border on GUI screen , sideways
		       pady=20,                      # space b/w  text  and border on GUI screen , above-below
		       image=logo,
		       compound='bottom'              #  printing  image on GUI screen at bottom
		  )
buttonNew.place(x=50,y=50)     # placing    text on GUI screen using coordinates 
           
windowNew.mainloop()
# displaying the GUI
