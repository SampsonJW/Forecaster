import json
import requests
import tkinter

APIcall = 'http://api.openweathermap.org/data/2.5/weather?q={},NZ&mode=json&units=metric&cnt=5&APPID=eaf254b78fb79221fb9747d92329ac53'

class Test(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

def get_weather():
    weather = requests.get(APIcall.format(input()))
    raining = Test(weather.text).weather[0]['description']
    temp = Test(weather.text).main['temp']
    show_weather(temp)

def show_weather(str):
    window = tkinter.Tk()
    window.minsize(150, 100)
    window.title("Weather")
    label = tkinter.Label(window, text = str).pack()
    window.mainloop()

get_weather()