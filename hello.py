
import datetime
from telebot import types
import telebot
# pip install pytelegrambotapi

bot = telebot.TeleBot("5733303924:AAGgd1P7Aau-9Iyl7YZGAh74SdE9AJUWC5s")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "/button")


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Сделать предложение")
    but2 = types.KeyboardButton("узнать время")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


@bot.message_handler(content_types="text")
def controller(message):
    print(message.text)
    if message.text == "Сделать предложение":
        bot.send_message(message.chat.id, "введи имя фамилию")
        bot.register_next_step_handler(message, sentence)
    elif message.text == "узнать время":
        bot.send_message(
            message.chat.id, f"текущее время - {datetime.datetime.now()}")
        button(message)


def sentence(message):
    text = message.text
    surname = text.split()[0]
    name = text.split()[1]
    bot.send_message(
        message.chat.id, f"Вас зовут - {name}, фамилия - {surname}")
    button(message)


bot.infinity_polling()


# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"
