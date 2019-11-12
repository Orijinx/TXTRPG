import config
import DATA
import Client
import time

dat = DATA.f_Order

def Write_CSV(D):
  try:
   with open('Orders.csv', 'a') as fCSV:
       for i in range(len(D)):
           fCSV.write(str(D[i]))
           fCSV.write(';')
       fCSV.write('\n')
       fCSV.close()

   print('Done:' + str(format( time.localtime())))
  except:
      print('Error')

Write_CSV(dat);