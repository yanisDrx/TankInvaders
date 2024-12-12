"""Classe Base_Canvas
Par : Pirès-Portelada Yanis et Bovet Gauthier
Lieu : CPE Lyon
Date : 18 Novembre 2024
Codé en : Python sur VS code"""

from tkinter import *


class Base_Canvas(Canvas): #Classe de la canvas principale
    
    def __init__(self,parent,bg_image):
        super().__init__(parent)
        
        self.configure(width=800, height=800) 
        
        self.bg_image = PhotoImage(file=bg_image)
        self.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        self.pack()