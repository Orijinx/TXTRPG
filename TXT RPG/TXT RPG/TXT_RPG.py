import config
import telebot
import socket
import socks
import time
import html


#ip = '178.197.249.213'  # change your proxy's ip
#port = 1080  # change your proxy's port
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
#socket.socket = socks.socksocket


bot = telebot.TeleBot(config.token)
mgameboard= telebot.types.ReplyKeyboardMarkup()
startboard= telebot.types.ReplyKeyboardMarkup()
mgameboard.resize_keyboard=True
startboard.resize_keyboard=True
mgameboard.row('Отправиться на пару', 'Пойти в столовую','Выйти покурить','Отправиться в другой корпус')
startboard.row('Я готов','Объясни как играть?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я - Бот курсача!.\nЯ проведу вас по пути студента, готовы ли вы отправиться в путешествие?',reply_markup=startboard)

@bot.message_handler(content_types=['text'])
def help_message(message):
    if message.text.lower() == 'объясни как играть?':
        bot.send_message(message.chat.id, 'Вы - студент КФ МГТУ. Ваша цель - отучиться курсю.\nДля выполнения этой цели, вы должны сдать три экзамена, два зачета и одну курсовую работу.\n После начала игры вы попадаете в 5 корпус. Это начало игры.\n Из контекстного меню, вы можете выбирать действия, которые желаете совершить.\nВсего существует три корпуса. В каждом корпусе находится некоторое количестов зачетов, экзаменов и ссылок на википедию для курсовой. После получения минимума (Оценки 3 по всем дисциплинам), ваше путешествие переходит в следующий корпус.\n И помни: Покайся! ')
    elif message.text.lower() == 'я готов':
            bot.send_message(message.chat.id, 'Добро пожаловать в лучшее учебноее завдение страны! Сегодня твой первый день. Лишь от тебя зависит закончишь ли ты обучение или отчислишься через неделю.')
            time.sleep(2)
            bot.send_photo(message.chat.id,config.img)
            bot.send_message(message.chat.id,'Я в пятом корпусе. Сегодня солнечно, студенты еще не устали. На улице поют птицы. Чем сегодня займемся?',reply_markup=mgameboard)
    

bot.polling()