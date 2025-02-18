import customtkinter as ctk
from .side_bar import menu
from ..read_json import read_json

list_city = read_json('config.json')["list_city"]

class CityFrame(ctk.CTkFrame):
    def __init__(self, city_name: str, master_ch: ctk.CTkScrollableFrame):
        ctk.CTkFrame.__init__(
            self,
            master = master_ch,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#b5d3d9",
            corner_radius = 20,
            fg_color = "#096C82"
        ) 
        self.pack(pady = 20)
        # CTkLabel - создает текст
        self.TEMP = ctk.CTkLabel(
            text = "-8°",
            master = self,
            font = ("Roboto Slab", 50, "bold"),
            text_color = "#FFFFFF"
        )
        self.TEMP.place(x = 155, y = 4)
        self.CITY = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 16, "bold"),
            text = str(city_name),
            text_color = '#FFFFFF'
        )
        self.CITY.place(x = 15, y = 12)
        self.TIME = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12, "bold"),
            text = '12:30',
            text_color = '#FFFFFF',
            height = 18
        )
        self.TIME.place(x = 15, y = 33)
        self.DESC = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12),
            text = 'Description.',
            text_color = '#b5d3d9'
        )
        self.DESC.place(x = 15, y = 70)
        self.TEMP_MIN_MAX = ctk.CTkLabel(
            master = self,
            font = ("Roboto Slab", 12),
            text = "макс: 11°, мін: 4°",
            text_color = '#b5d3d9'
        )
        self.TEMP_MIN_MAX.place(x = 126, y = 70)

for city_name in list_city:
    city = CityFrame(city_name, menu)