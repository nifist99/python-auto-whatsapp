from profider.telkomsel import Telkomsel
import imp
import random
import string
import pywhatkit


class TelkomselController:
    def jawatimur(pesan,link,name):
        profider = Telkomsel.jawatimur()
        op=random.sample(profider,1)
        result=" ".join(op)
        print(result)
        if(len(str(result))==5):
            ran=random.randint(1000000, 9999999)
        elif(len(str(result))==6):
            ran=random.randint(100000, 999999)
        elif(len(str(result))==7):
            ran=random.randint(10000, 99999)
        elif(len(str(result))==8):
            ran=random.randint(1000, 9999)
        number =result+""+str(ran)
        print(number.replace("0","+62",1))
        pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), pesan+"\n\n"+name+"\n\n"+link, 10, tab_close=True)

    def sumatera(pesan,link,name):
        profider = Telkomsel.sumatera()
        op=random.sample(profider,1)
        result=" ".join(op)
        print(result)
        if(len(str(result))==5):
            ran=random.randint(1000000, 9999999)
        elif(len(str(result))==6):
            ran=random.randint(100000, 999999)
        elif(len(str(result))==7):
            ran=random.randint(10000, 99999)
        elif(len(str(result))==8):
            ran=random.randint(1000, 9999)
        number =result+""+str(ran)
        print(number.replace("0","+62",1))
        pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), pesan+"\n\n"+name+"\n\n"+link, 10, tab_close=True)