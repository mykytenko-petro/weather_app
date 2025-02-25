import customtkinter as ctk
from .main_screen import app

class Info(ctk.CTkFrame):
    def __init__(self, child_master: ctk.CTk):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 925,
            height = 800,
            fg_color = "#5DA7B1"
        )
        self.grid(row = 0, column = 1)
        
        self.current_position = ctk.CTkLabel(
            master = self,
            text = 'Поточна позицiя',
            font = ('Roboto Slab', 35, 'bold'),
            text_color = '#FFFFFF'
        )
        self.current_position.place(x = 310, y = 100)

info = Info(child_master = app)