# 5921040825:AAFL8U5nV65wwV2brIEV1O5A3NbrQGH8SrE
from telebot import types
import telebot
bot = telebot.TeleBot("5921040825:AAFL8U5nV65wwV2brIEV1O5A3NbrQGH8SrE")
# group_2bot


@bot.message_handler(commands=["start"])
def start(message):
    # bot.send_message(message.chat.id, "/button")
    bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(message, sentence)


def sentence(message):
    text = message.text
    bot.send_message(message.chat.id, f"Вас зовут - {text}, хотите сыграть?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да")
    but2 = types.KeyboardButton("нет")
    markup.add(but1)
    markup.add(but2)
    # bot.register_next_step_handler(message, AnswerYes)


@bot.message_handler(content_types="text")
def controller(message):
    print(message.text)
    if message.text == "Да":
        bot.send_message(message.chat.id, "Возьмите конфеты от 1 до 28")
        bot.register_next_step_handler(message, PlayGame)
    elif message.text == "нет":
        bot.send_message(
            message.chat.id, f"выход")
        button(message)


def PlayGame(message):
    bot.send_message(message.chat.id, f"Вы взяли {message.text}  конфет")
    bot.register_next_step_handler(message, nextStep)


def NextStep():
    print('fdsf')


    # def ShowMenu():
bot.infinity_polling()

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

# import datetime
# from telebot import types
# import telebot
# # pip install pytelegrambotapi

# bot = telebot.TeleBot("5733303924:AAGgd1P7Aau-9Iyl7YZGAh74SdE9AJUWC5s")


# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "/button")


# @bot.message_handler(commands=["button"])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     but1 = types.KeyboardButton("Сделать предложение")
#     but2 = types.KeyboardButton("узнать время")
#     markup.add(but1)
#     markup.add(but2)
#     bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


# @bot.message_handler(content_types="text")
# def controller(message):
#     print(message.text)
#     if message.text == "Сделать предложение":
#         bot.send_message(message.chat.id, "введи имя фамилию")
#         bot.register_next_step_handler(message, sentence)
#     elif message.text == "узнать время":
#         bot.send_message(
#             message.chat.id, f"текущее время - {datetime.datetime.now()}")
#         button(message)


# def sentence(message):
#     text = message.text
#     surname = text.split()[0]
#     name = text.split()[1]
#     bot.send_message(
#         message.chat.id, f"Вас зовут - {name}, фамилия - {surname}")
#     button(message)


# bot.infinity_polling()
