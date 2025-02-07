import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, name: str, width: int, height: int):
        ctk.CTk.__init__(
            self = self
        )
        self.title(string = name)
        self.geometry(f'{width}x{height}')
app = App(name = 'Weather App', width = 1200, height = 800)
