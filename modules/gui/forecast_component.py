import customtkinter as ctk
from .forecast_frame import *
from ..weather_data import get_info_weather
from ..read_json import read

get_info_weather("Дніпро", "forecast.json", True)
list_weather = read("forecast.json")["list"]

class ForecastComponent(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkScrollableFrame, count: int):
        ctk.CTkFrame.__init__(
            self, 
            master, 
            fg_color="#5DA7B1"
        )
        self.grid(row = 0, column = count, padx = 35)
        data = list_weather[count]
        temp = round(data['main']['temp'])
        self.TEMP = ctk.CTkLabel(
            self, 
            text = f'{temp}°',
            font = ('Inter', 30, 'bold')
        )
        self.TEMP.pack(pady = 25)
        
for index in range(len(list_weather)):
    comp = ForecastComponent(forecast, index)