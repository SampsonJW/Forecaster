import json
import requests
import tkinter as tk

APIcall = 'http://api.openweathermap.org/data/2.5/weather?q={},NZ&mode=json&units=metric&cnt=5&APPID=eaf254b78fb79221fb9747d92329ac53'

root = tk.Tk()
root.minsize(720,480)
root.title('Weather')
root.configure(background="white")
frame = tk.Frame(root)
frame.configure(background="white")
frame.pack()

label = tk.Label(frame, background = "white", text = 'Enter your city:').pack()
cityEntry = tk.Entry(frame,background = "white")
cityEntry.pack()

def show_weather(weatherDict):
    tk.Label(frame, background = "white", text = "Conditions: " + weatherDict['rain']).pack()
    tk.Label(frame, background = "white", text = "Temperature: " + str(weatherDict['temp'])).pack()


class Test(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

def get_weather():
    
    weather = requests.get(APIcall.format(cityEntry.get()))
    raining = Test(weather.text).weather[0]['description']
    temp = Test(weather.text).main['temp']
    weathDict = {'temp': temp, 'rain': raining}
    show_weather(weathDict)

b = tk.Button(frame, background = "white", text='Go', command = get_weather).pack()

root.mainloop()
