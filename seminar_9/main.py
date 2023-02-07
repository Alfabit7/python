from telebot import types
import telebot
import random
TOKEN=''
bot = telebot.TeleBot(TOKEN)

candies = 99
maxStep = 28
name = ''
whoseMove = ''


@bot.message_handler(commands=['start'])
def start(message):
    but1 = types.KeyboardButton("Да")
    but2 = types.KeyboardButton("Нет")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(but1)
    markup.add(but2)
    bot.send_message(
        message.chat.id, f'Привет! Хочешь сыграть в игру конфеты?', reply_markup=markup)
    bot.register_next_step_handler(message, PlayOrNotPlay)


def PlayOrNotPlay(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Давай сыиграем, как тебя зовут?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, UserNameRequest)
    else:
        bot.send_message(message.chat.id, 'Жаль! Если захочешь сыграть пиши /start',
                         reply_markup=types.ReplyKeyboardRemove())


def UserNameRequest(message):
    global name
    name = message.text
    but1 = types.KeyboardButton("Да")
    but2 = types.KeyboardButton("Нет")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(but1)
    markup.add(but2)
    bot.send_message(
        message.chat.id, f'{name} ты знаешь правила игры?', reply_markup=markup)
    bot.register_next_step_handler(message, QuestionRulesGame)


def QuestionRulesGame(message):
    global name, whoseMove, candies
    whoseMove = random.choice(['user', 'bot'])
    if whoseMove == 'user':
        player = name
    else:
        player = 'bot'
    if message.text == 'Да':
        bot.send_message(
            message.chat.id, f'Тогда погнали! {name}  ))\n Всего конфет {candies} Максимально можно взять {maxStep} ')
        bot.send_message(
            message.chat.id, f'Жеребьевка показала, что первым ходит {player}')
        controller(message)
    else:
        bot.send_message(
            message.chat.id, f'{name} правила очень легкие! \n В коробке лежат {candies} конфет\n Каждый игрок, почередно берет конфеты, \n брать можно от 1 штуки до {maxStep} штук \n Побеждает тот игрок, кто заберет последние конфеты \n')
        bot.send_message(
            message.chat.id, f'Жеребьевка показала, что первым ходит {player}')
        controller(message)


def controller(message):
    global whoseMove, stepUser, stepBot, player, name, candies
    if candies > 29:
        if whoseMove == 'user':
            player = name
            bot.send_message(
                message.chat.id, f'Всего конфет {candies}, {player} возьмите конфеты от 1 до {maxStep}')
            bot.register_next_step_handler(message, InputUser)
        else:
            player = 'bot'
            bot.send_message(message.chat.id, f' ходит {player}')
            InputBot(message)
    else:
        if candies < 29:
            if player == name:
                player = 'bot'
            else:
                player == 'bot'
                player = name
        bot.send_message(message.chat.id, f'Победил {player}')
        bot.send_message(
            message.chat.id, f'Сыграем еще раз? Пиши старт /start')
        candies = 99


def InputUser(message):
    global candies, player, maxStep, whoseMove, stepBot, stepUser
    while True:
        try:
            stepUser = int(message.text)
            if 0 < stepUser < 29:
                candies -= stepUser
                bot.send_message(
                    message.chat.id, f' {player} Вы взяли {stepUser} конфет, осталось {candies} конфет')
                whoseMove = 'bot'
                controller(message)
                break
            else:
                bot.send_message(
                    message.chat.id, f'только числа от 1 до 28 введите правильное значение!!! ')
                bot.register_next_step_handler(message, InputUser)
                break

        except:
            bot.send_message(
                message.chat.id, f'Вводить можно только числа от 1 до 28 введите правиьное значение')
            bot.register_next_step_handler(message, InputUser)
            break


def InputBot(message):
    global candies, player, maxStep, whoseMove, stepBot, stepUser, name
    stepBot = random.randint(1, 29)
    bot.send_message(
        message.chat.id, f'{player} взял {stepBot} конфет, осталось {candies-stepBot} ')
    candies -= stepBot
    whoseMove = 'user'
    bot.send_message(message.chat.id, f'Теперь ходит {name}')
    controller(message)


bot.infinity_polling()
