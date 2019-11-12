import DATA

Kursach_token = '734924842:AAFMvyjdkG2aMDNMKrU-IPnbcp52_lZ260A'
token_client = '728368201:AAHv_hyxsDvqzyentj44I0ecmO-yJkSVkAM'
payments_token = '381764678:TEST:11798'
#assets = r'C:\Users\Acer\Pictures\Saved Pictures'
#img=open(assets + r'\5Kin.jpg','rb')


#параметры состояния
inWork = False
isGameStart = False 


class Player(object):
    def __init__(self,Login,GS,W):
       self.Login = Login
       self.GS = GS
       self.W = W
    def GetGameState():
        return GS, W
        
class User(object):
    def __init__(self, *args, **kwargs):
        self.ID
        #DATA.MaOr
    def getID(self):
        return self.ID

class Order(object):
    def __init__(self, *args, **kwargs):
        self.Item
        self.Val
        self.Adr
        self.Us


class proxy1:
    ip = "69.4.86.195"
    port = 42063

class proxy2:
    ip = '207.154.231.211'
    port = 		1080

class char:
    starv=0
    sleep=0
    inte=0
    stress=0

  
