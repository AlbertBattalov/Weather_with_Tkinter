from tkinter import ttk

import requests
from tkinter import messagebox
from ttkthemes import ThemedTk
import time


def get_result_weather():
    if not city_entry.get():
        messagebox.showinfo('Неверно совершен запрос', 'Введите название города ')
    else:
        parameters = {
            'appid': API_key_weather,
            'q': city_entry.get(),
            "units": "metric",
            "lang": 'ru'
        }
        r = requests.get(API_URL, params=parameters)
        weather = r.json()
        label['text'] = get_data(weather)


def get_data(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temperature = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise = weather['sys']['sunrise']
        sunset = weather['sys']['sunset']
        sunrise_local = time.localtime(sunrise)
        sunset_local = time.localtime(sunset)
        sunrise_normal = time.strftime('%H:%M:%S', sunrise_local)
        sunset_normal = time.strftime('%H:%M:%S', sunset_local)
        return f'Местоположение: {city},{country} \n Температура: {temperature} по Цельсию\nАтомсферное давление: {press}\nВлажность воздуха: {humidity}\nСкорость ветра: {wind} м/с\nОбщее описание погоды: {desc}\nВосход солнца: {sunrise_normal}\nЗакат солнца: {sunset_normal}\n'
    except:
        return "Нет данных о погоде в данном городе"


API_key_weather = 'f718ac5f2a80fc4f9aa7e6adf79d9e16'
API_URL = 'https://api.openweathermap.org/data/2.5/weather' \
    # api.openweathermap.org/data/2.5/weather?appid={API key}&q={kumertau,rf}
root = ThemedTk(theme='arc')
root.geometry('500x400+400+300')
root.resizable(None)
top_Frame = ttk.Frame(root)
top_Frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1,
                anchor='n')
city_entry = ttk.Entry(top_Frame)
city_entry.place(relwidth=0.7, relheight=1)

btn1 = ttk.Button(top_Frame, text='Запрос погоды', command=get_result_weather)
btn1.place(relx=0.7, relwidth=0.3, relheight=1)
low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6,
                anchor='n')
label = ttk.Label(low_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

root.mainloop()
