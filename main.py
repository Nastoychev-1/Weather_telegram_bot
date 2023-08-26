import json

import telebot
import requests

bot = telebot.TeleBot('6572118557:AAE_hBzzWC2M3-nGOf8HVqY8tDqwKTxYTQE')
#Токен бота
API = '20352a7df4ca4bfe1b2719cf4e8db8f3'
#Токен для атображения актульной погоды

@bot.message_handler(commands=['start'])
def say_hi(message):#Функция для ответа пользавотелю
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name + '.Напиши название города!')

@bot.message_handler(content_types=['text'])
def get_weather(message):#Функция для вывода погоды
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        bot.reply_to(message, f'Сейчас погода: {temp}, по цельсию.'
                              f'Минимальная:{temp_min}.Максимальная:{temp_max}')

        image = 'sun.png' if temp > 20.0 else 'sunny.png'#Условие для выбора правильной картинки
        file = open('./' + image, 'rb')#Преобразование формата
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Неверно указан город')

bot.polling(none_stop=True)