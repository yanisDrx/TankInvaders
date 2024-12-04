from tkinter import *


class Buttons(Button): #Classe des boutons principaux
    
    def __init__(self,parent,text,command,xaxis,yaxis):
        super().__init__(parent)
        
        self.text=text
        self.command=command
        self.xaxis=xaxis
        self.yaxis=yaxis
        
        self.button_style = {
            "font": ("Arial", 18, "bold"),
            "bg": "#878787",
            "fg": "white",
            "activebackground": "lightgrey",
            "activeforeground": "white",
            "relief": "raised",
            "bd": 1,
            "width": 17,
            "height": 1
        }
        
        self.configure(text=self.text, command=self.command, **self.button_style)
        
        self.place(x=xaxis, y=yaxis)