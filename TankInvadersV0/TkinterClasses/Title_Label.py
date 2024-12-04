from tkinter import *


class Title_Text(Text):
    def __init__(self, parent, canvas, text, colour, xaxis, yaxis):
        super().__init__(parent)
        
        self.title_style = {
            "font": ("Arial", 50, "bold"),
            "fill": colour,  # Couleur du texte
        }
        
        canvas.create_text(
            xaxis, yaxis,
            text=text,
            font=self.title_style["font"],
            fill=self.title_style["fill"],
            anchor="center")