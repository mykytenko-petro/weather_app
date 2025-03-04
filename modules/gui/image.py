import PIL.Image
import customtkinter as ctk
from ..read_json import *
from .main_screen import *
from ..weather_data import *

# PIL (Pillow) - модуль для роботы с картинками

class WeatherImage(ctk.CTkLabel):
    def __init__(self, width: int, height: int, master: ctk.CTk | ctk.CTkFrame, name_json: str):
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_JSON = name_json
        ctk.CTkLabel.__init__(
            self,
            master,
            text = "",
            image = self.load_img()
        )
    def load_img(self):
        data_weather = read(self.NAME_JSON)
        name_image = data_weather["weather"][0]["icon"]
        path_image = os.path.abspath(__file__ + f'/../../../images/{name_image}.png')
        # PIL.Image.open - открывает/создает картинку 
        image = PIL.Image.open(fp = path_image)
        return ctk.CTkImage(
            image,
            size = (self.WIDTH,self.HEIGHT)
        )

first_city = read("config.json")["list_city"][0]
get_info_weather(first_city)
main_image = WeatherImage(170, 160, app, 'weather_data.json')
main_image.place(x = 380, y = 170)