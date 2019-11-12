# -*- coding: utf-8 -*-


##########Main###############
import DATA
import config
import telebot
import ShopFunction
from telebot import types
from telebot.types import LabeledPrice, ShippingOption
########Add###################
import socks
import socket
import subprocess
import sys


#############CreateBot##########
bot = telebot.TeleBot(config.token_client)

#try:
#    ip = config.proxy2.ip
#    port = config.proxy2.port
#    socks.set_default_proxy(socks.SOCKS4, "103.58.16.254",4145)
#    socket.socket = socks.socksocket
#except:
#   print('Connecting out')

#########Var######################
Users = config.User

#############keyboard#############
get_order_keyboard = telebot.types.ReplyKeyboardMarkup()
get_order_keyboard.resize_keyboard = True
get_order_keyboard.row('Каталог','/info','QR-order')

Y_N = telebot.types.ReplyKeyboardMarkup()
Y_N.resize_keyboard = True
Y_N.row('Да','Нет')


STATE_DICT = {}
MaOr = []
prices = [LabeledPrice(label='Дерьмо', amount=5750),]
OrderList =""
Data_writer_off = True

########Hendler####################
@bot.message_handler(commands=['start'])
def start_message(message):
    Users.ID=message.from_user.id
    DATA.User_Data.append(Users)
    bot.send_message(message.chat.id, 'Отлично! Вы создали аккаунт:' + str(DATA.User_Data[0].ID) + ' Давайте начнем!ы', reply_markup=get_order_keyboard)

@bot.message_handler(commands=['info'])
def getAccInfo(message):
 #try:
    OrderList=''
    for i in range(len(DATA.User_Data)):
        if DATA.User_Data[i].ID == message.from_user.id:
            bot.send_message(message.chat.id,'Информация о пользователе:' + str(DATA.User_Data[i].ID))
            for j in range(len(DATA.Proceed_Order)):
                print('['+ str(j) + ']' +'[' + str (DATA.Proceed_Order[j].index(message.from_user.id)) + ']' )
                if DATA.Proceed_Order[j].index(message.from_user.id) !=0: 
                    OrderList += str(DATA.Proceed_Order[j]) + '\n'
            bot.send_message(message.chat.id,'Заказы:' + str(OrderList) )
        else:
            bot.send_message(message.chat.id,'Вы еще не зарегестрированы!')
 #except:
   #  print('No atribute')

@bot.message_handler(commands=['buy'])
def command_pay(message):
    bot.send_message(message.chat.id,"Я - в дерьме", parse_mode='Markdown')
    bot.send_invoice(message.chat.id, title='Дерьмо',
                     description='Ну, реально, просто... гавно...',
                     provider_token=config.payments_token,
                     currency='rub',
                     photo_url='https://a.d-cd.net/2EAAAgKYdOA-1920.jpg',
                     photo_height=512,  # !=0/None or picture won't be shown
                     photo_width=512,
                     photo_size=512,
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     prices=prices,
                     start_parameter='time-machine-example',
                     invoice_payload='HAPPY FRIDAYS COUPON')



@bot.message_handler(content_types=['text'])
def Start_work(message):
    if message.text.lower() == 'каталог':
        Cut = ''
        for i in range(len(DATA.Cut)):
            Cut = Cut + '\n' + ShopFunction.Print_List_of_Cut(i)
        bot.send_message(message.chat.id,Cut)
        bot.send_message(message.chat.id,'Готовы оформить заказ?', reply_markup=Y_N)
        bot.register_next_step_handler(message,Order)


def Order(message):
 for i in range(len(DATA.User_Data)):
        if DATA.User_Data[i].ID == message.from_user.id:
            UsEr = DATA.User_Data 
 #if UsEr.id ==  message.from_user.id: 
 if message.text.lower() == 'да':
        bot.send_message(message.chat.id,'Укажите ID товара, который вы хотите заказать')
        bot.register_next_step_handler(message,Make_Order_Value)
       
 elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id,'Главное меню',reply_markup=get_order_keyboard)
       # bot.register_next_step_handler(message,Start_work)
 #except:
 #    bot.send_message(message.chat.id, 'Вы еще не зарегестрированы! Пройти регистрацию?',reply_markup = Y_N)
 #    bot.register_next_step_handler(message, Regestration)




def Make_Order_Value(message):
      Lot_ID = int(message.text)
      DATA.MaOr.append(str(DATA.Cut[Lot_ID-1]))
      bot.send_message(message.chat.id,'Укажите колличество')
      bot.register_next_step_handler(message, Make_Order_Adres) 


def Make_Order_Adres(message):
    DATA.MaOr.append(str(message.text))
    bot.send_message(message.chat.id,'Напишите точный адрес доставки \nПрим:Калуга, ул.Труда 9, кв.5')
    bot.register_next_step_handler(message,Make_Order_Done)


def Make_Order_Done(message):
     DATA.MaOr.append(str(message.text))
     DATA.MaOr.append(message.from_user.id)
     print(DATA.MaOr)
     DATA.Proceed_Order.append(DATA.MaOr)
     bot.send_message(message.chat.id,'Ваш заказ успешно сформирован! Ожидайте \n Информация о заказе:' + str(DATA.MaOr),reply_markup = get_order_keyboard )
     if Data_writer_off:
         DATA.MaOr.reverse
         #print(str(DATA.MaOr[0]))
         Memory_Writer(DATA.MaOr[0])
         DATA.MaOr.reverse
     else:
         print('Writer_is_on')



def  Regestration(message):
     if message.text.lower() == 'да':
        bot.next_step_handlers(start_message)

def Memory_Writer(data):
    print(str(data))
    DATA.f_Order = data
    subprocess.Popen([sys.executable, 'Sub_Proc/f_writer.py'])









if __name__ == "__main__":
    bot.polling(none_stop=True)




