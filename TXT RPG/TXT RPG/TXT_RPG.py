import config
import telebot
import socket
import socks
import time

try:
    ip = config.proxy2.ip
    port = config.proxy2.port
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket
except ConnectionError:
    ip = config.proxy2.ip
    port = config.proxy2.port
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket


bot = telebot.TeleBot(config.token)
mgameboard= telebot.types.ReplyKeyboardMarkup()
startboard= telebot.types.ReplyKeyboardMarkup()
mgameboard.resize_keyboard=True
startboard.resize_keyboard=True
mgameboard.row('Отправиться на пару', 'Пойти в столовую','Выйти покурить','Проверить характеристики')
startboard.row('Я готов','Объясни как играть?')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я - Бот курсача!.\nЯ проведу вас по пути студента, готовы ли вы отправиться в путешествие?',reply_markup=startboard)
    config.char.starv=100
    config.char.sleep=0
    config.char.inte=50
    config.char.stress=0

@bot.message_handler(content_types=['text'])
def help_message(message):
    if message.text.lower() == 'объясни как играть?':
        bot.send_message(message.chat.id, 'Вы - студент КФ МГТУ. Ваша цель - отучиться курсю.\nДля выполнения этой цели, вы должны сдать три экзамена, два зачета и одну курсовую работу.\n После начала игры вы попадаете в 5 корпус. Это начало игры.\n Из контекстного меню, вы можете выбирать действия, которые желаете совершить.\nВсего существует три корпуса. В каждом корпусе находится некоторое количестов зачетов, экзаменов и ссылок на википедию для курсовой. После получения минимума (Оценки 3 по всем дисциплинам), ваше путешествие переходит в следующий корпус.\n И помни: Покайся! ')
    elif message.text.lower() == 'я готов':
            bot.send_message(message.chat.id, 'Добро пожаловать в лучшее учебноее завдение страны! Сегодня твой первый день. Лишь от тебя зависит закончишь ли ты обучение или отчислишься через неделю.')
            time.sleep(2)
            bot.send_message(message.chat.id,'https://versiya.info/uploads/posts/2018-10/1540215615_11781.jpg')
            bot.send_message(message.chat.id,'Я в пятом корпусе. Сегодня солнечно, студенты еще не устали. На улице поют птицы. Чем сегодня займемся?',reply_markup=mgameboard)
    elif message.text.lower() == 'отправиться на пару':
        bot.send_message(message.chat.id,'http://vladivostok.mger2020.ru/sites/default/files/users/user1898/_dsc9941.jpg')
        bot.send_message(message.chat.id, 'Пара прошла мимо вас. Вы просрали 2ч, но получили +2 к учебе. -2Ч +2И +3У -1C +1С')
        config.char.starv=config.char.starv-1
        config.char.sleep=config.char.sleep+3
        config.char.inte=config.char.inte+2
        config.char.stress=config.char.stress+1
    elif message.text.lower() == 'Выйти покурить':
        bot.send_message(message.chat.id,'https://www.aziaminvatat.ro/images/aai-images/aai-9510-2.jpg')
        bot.send_message(message.chat.id, 'Вы вышли покурить. Вы поболтали со знакомыми 30минут и получили -2 к стрессу. -0,5Ч +0И +1У -2C -2С')
        config.char.starv=config.char.starv-2
        config.char.sleep=config.char.sleep+1
        config.char.stress=config.char.stress-2
    elif message.text.lower()=='проверить характеристики':
         bot.send_message(message.chat.id, 'Сытость:'+ str(config.char.starv) + ' Усталость:' + str(config.char.sleep) + ' Интеллект:' + str(config.char.inte) + ' Стресс:' +str(config.char.stress))
    elif message.text.lower() == 'пойти в столовую':
        bot.send_message(message.chat.id,'https://fastly.4sqi.net/img/general/600x600/21664938_4gAQshNBxjmAZOMt2EcX5Np1ZqAUHQvnowm7DxDQYs4.jpg')
        bot.send_message(message.chat.id, 'В столовке была очередь, и вы потратили всю перемену. Зато силы восстановлены! +2 к сытости, -1 к интелекту, -1 к стрессу')
        config.char.starv=config.char.starv+2
        config.char.inte=config.char.inte-1
        config.char.stress=config.char.stress-1
bot.polling()
