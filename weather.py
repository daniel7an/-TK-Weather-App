import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=30bd326b4b202b2a3fb5327fe69e5624"
    json_data = requests.get(api).json()
    
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    temp_min = int(json_data["main"]["temp_min"])
    temp_max = int(json_data["main"]["temp_max"])

    label1.config(text = f"Wather is: {str(condition)} \n Minimal Temperature is: {str(temp_min)} \n Maximal TEmperature is: {str(temp_max)}")


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = f)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()


