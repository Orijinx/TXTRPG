import telebot
import DATA
import Client
import threading
from threading import Lock
lock = Lock()

def Print_List_of_Cut(index):
   Order_Info = 'Название:' + str(DATA.Cut[index][0] )+ ' Цена:' + str(DATA.Cut[index][1]) + ' Магазин:' + str(DATA.Cut[index][2]) + 'Номер для заказа:' + str(DATA.Cut[index][3])
   return Order_Info


def CSV():
    lock.acquire()
    try:
        fCSV = open('Orders.csv','a')
        print('Locale fCSV')
    except:
        fCSV = open('Orders.csv','w')
        print('Create fCSV')
    for j in range(len(DATA.MaOr)):
        for k in range(2):
            fCSV.write(DATA.Order_inf[k] )
            fCSV.write(';')
            fCSV.write(str(DATA.MaOr[j]))
            try:
               fCSV.write(DATA.MaOr[j][k] )
            except:
              fCSV.write(str(DATA.MaOr[j][k]))
            fCSV.write(';') 
            fCSV.close()




@Client.bot.message_handler(func= lambda message:True)
def Make_Order_Value(message):
      Lot_ID = int(message.text)
      DATA.MaOr.append(DATA.Cut[Lot_ID-1])
      Client.bot.send_message(message.chat.id,'Укажите колличество')
      Client.bot.next_step_saver(Client.Get_Value) 


def Make_Order_Adres(message):
    DATA.MaOr.append(message.text)
    Client.bot.send_message(message.chat.id,'Напишите точный адрес доставки \nПрим:Калуга, ул.Труда 9, кв.5')
    Client.bot.register_next_step_handler(message,Make_Order_Done)

def Make_Order_Done(message):
     DATA.MaOr.append(message.text)
     DATA.MaOr.append(message.from_user.id)
     print(DATA.MaOr)
     DATA.Proceed_Order.append(DATA.MaOr)
     Client.bot.send_message(message.chat.id,'Ваш заказ успешно сформирован! Ожидайте \n Информация о заказе:' + str(DATA.MaOr))

    



