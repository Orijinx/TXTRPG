import socket
import time
from multiprocessing import Queue
import socks
import telebot
import config
#Создание соединения и бота
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

# Создание соединения и бота
# try:
# ip = config.proxy2.ip
# port = config.proxy2.port
# socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket
# except ConnectionError:
#    ip = config.proxy2.ip
#   port = config.proxy2.port
 #  socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, ip, port)
  # socket.socket = socks.socksocket
bot = telebot.TeleBot(config.token)

# Описание переменных
Users = config.Player('', '', '')
BufUsers = config.Player('', '', '')
Q = Queue()
# Описание клавиатур
mgameboard = telebot.types.ReplyKeyboardMarkup()
startboard = telebot.types.ReplyKeyboardMarkup()
mgameboard.resize_keyboard = True
startboard.resize_keyboard = True
# mgameboard.row_width=20
mgameboard.row('Отправиться на пару', 'Пойти в столовую',
               'Выйти покурить', 'Проверить характеристики')
startboard.row('Я готов', 'Объясни как играть?')


def GameOver(message):
    if config.char.starv == 0:
        config.isGameStart = False
        bot.send_message(
            message.chat.id, 'Вы упали в обморок и сдохли от голода. КОНЕЦ ИГРЫ!')
    elif config.char.starv >= 100:
        config.char.starv = 100

    elif config.char.sleep == 100:
        config.isGameStart = False
        bot.send_message(
            message.chat.id, 'Соснул на паре. Отчислили. КОНЕЦ ИГРЫ!')
    elif config.char.sleep <= 0:
        config.char.sleep = 0

    elif config.char.inte <= 0:
        config.isGameStart = False
        bot.send_message(
            message.chat.id, '-Вы тупой. СКазали вам в деканате и отчислили. КОНЕЦ ИГРЫ!')
    elif config.char.inte >= 100:
        config.isGameStart = False
        bot.send_message(
            message.chat.id, 'Вы осознали,что этот универ - шарага и отчислились самостоятельно. КОНЕЦ ИГРЫ!')

    elif config.char.stress == 100:
        config.isGameStart = False
        bot.send_message(
            message.chat.id, 'После очередного нервного срыва, вы совершили самоубийство')
    elif config.char.stress <= 0:
        config.char.stress = 0



        




@bot.message_handler(commands=['start'])
def start_message(message):
    config.isGameStart = True
    bot.send_message(
        message.chat.id, 'Здравствуйте, я - Бот курсача!.\nЯ проведу вас по пути студента, готовы ли вы отправиться в путешествие?', reply_markup=startboard)
    config.char.starv = 100
    config.char.sleep = 0
    config.char.inte = 3
    config.char.stress = 0
    Users.Login = message.from_user.id
    Users.GS = config.isGameStart
    Users.W = config.inWork
    Q.put(Users)


@bot.message_handler(content_types=['text'])
def help_message(message):
    BufUsers = Q.get()
    bot.send_message(message.chat.id, BufUsers.Login)
    while message.from_user.id != BufUsers.Login:
        Q.put(BufUsers)
        BufUsers = Q.get()
        bot.send_message(message.chat.id, 'Производится вход в игру')
    if BufUsers.GS:
                if BufUsers.W:
                    bot.send_message(message.chat.id, 'Вы заняты')
                elif message.text.lower() == 'объясни как играть?':
                    bot.send_message(message.chat.id, 'Вы - студент КФ МГТУ. Ваша цель - отучиться курсю.\nДля выполнения этой цели, вы должны сдать три экзамена, два зачета и одну курсовую работу.\n После начала игры вы попадаете в 5 корпус. Это начало игры.\n Из контекстного меню, вы можете выбирать действия, которые желаете совершить.\nВсего существует три корпуса. В каждом корпусе находится некоторое количестов зачетов, экзаменов и ссылок на википедию для курсовой. После получения минимума (Оценки 3 по всем дисциплинам), ваше путешествие переходит в следующий корпус.\n И помни: Покайся! ')
                elif message.text.lower() == 'я готов':
                    bot.send_message(
                        message.chat.id, 'Добро пожаловать в лучшее учебноее завдение страны! Сегодня твой первый день. Лишь от тебя зависит закончишь ли ты обучение или отчислишься через неделю.')
                    time.sleep(2)
                    bot.send_message(
                        message.chat.id, 'https://versiya.info/uploads/posts/2018-10/1540215615_11781.jpg')
                    bot.send_message(
                        message.chat.id, 'Я в пятом корпусе. Сегодня солнечно, студенты еще не устали. На улице поют птицы. Чем сегодня займемся?', reply_markup=mgameboard)
                elif message.text.lower() == 'отправиться на пару':
                    config.inWork = True
                    bot.send_message(message.chat.id, 'Вы отправились на пару')
                    time.sleep(10)
                    config.inWork = False
                    bot.send_message(
                        message.chat.id, 'http://vladivostok.mger2020.ru/sites/default/files/users/user1898/_dsc9941.jpg')
                    bot.send_message(
                        message.chat.id, 'Пара прошла мимо вас. Вы просрали 2ч, но получили +2 к учебе. -2Ч +2И +3У -1C +1С')
                    config.char.starv = config.char.starv - 10
                    config.char.sleep = config.char.sleep + 30
                    config.char.inte = config.char.inte + 20
                    config.char.stress = config.char.stress + 10
                    GameOver(message)
                elif message.text.lower() == 'выйти покурить':
                    config.inWork = True
                    bot.send_message(
                        message.chat.id, 'Вы - вейпер, как не стыдно то в 2к19?')
                    time.sleep(5)
                    config.inWork = False
                    bot.send_message(
                        message.chat.id, 'https://www.aziaminvatat.ro/images/aai-images/aai-9510-2.jpg')
                    bot.send_message(
                        message.chat.id, 'Вы поболтали со знакомыми 30минут и получили -2 к стрессу. -0,5Ч +0И +1У -2C -2С')
                    config.char.starv = config.char.starv - 20
                    config.char.sleep = config.char.sleep + 10
                    config.char.stress = config.char.stress - 20
                    GameOver(message)
                elif message.text.lower() == 'проверить характеристики':
                    bot.send_message(message.chat.id, 'Сытость:' + str(config.char.starv) + ' Усталость:' + str(
                        config.char.sleep) + ' Интеллект:' + str(config.char.inte) + ' Стресс:' + str(config.char.stress))
                elif message.text.lower() == 'пойти в столовую':
                    config.inWork = True
                    bot.send_message(message.chat.id, 'А где моя сосиска?')
                    time.sleep(5)
                    config.inWork = False
                    bot.send_message(
                        message.chat.id, 'https://fastly.4sqi.net/img/general/600x600/21664938_4gAQshNBxjmAZOMt2EcX5Np1ZqAUHQvnowm7DxDQYs4.jpg')
                    bot.send_message(
                        message.chat.id, 'В столовке была очередь, и вы потратили всю перемену. Зато силы восстановлены! +2 к сытости, -1 к интелекту, -1 к стрессу')
                    config.char.starv = config.char.starv + 20
                    config.char.inte = config.char.inte - 10
                    config.char.stress = config.char.stress - 10
                    GameOver(message)
    else:
                bot.send_message(message.chat.id, 'Чтобы начать играть - напиши /start')


bot.polling()
