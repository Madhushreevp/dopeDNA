# Tkinter

from tkinter import *
# importing all libraries of Tkinter

windowNew=Tk()
# create a window named windowNew

windowNew.geometry("343x343")
# defining size of window in terms of height and width

windowNew.title("New GUI Window")
# renaming window 

logo=PhotoImage(file="Aesthetic.png")
windowNew.iconphoto(True,logo)
# renaming window 

windowNew.config(background="Royal Blue")
# config window allows to make changes to window
# changing color of window to royal blue
 
windowNew.mainloop()
# displaying the GUI
