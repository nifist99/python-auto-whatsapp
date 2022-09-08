
import imp
import random
import string
import numpy as np
import pywhatkit
import requests
import time
from controller.XlController import Controller
 
        
def api(kode):
    API_ENDPOINT = "https://tokopedia.kedaiwoeloeng.com/api/affiliate"
  
    # data to be sent to api
    data = {'kode':kode}
    
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)
    
    # extracting response text 
    result = r.json()
    return result

# def process(pesan,link):
#     ran=random.randint(10000000, 99999999)
#     op=random.sample(new_operator,1)
#     result=" ".join(op)
#     number =result+""+str(ran)
#     print(number.replace("0","+62",1))
#     pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1),pesan+"\n\n"+link, 10, tab_close=True)

# # jumlah nomer 11
# def process2(pesan,link):
#     ran=random.randint(1000000, 9999999)
#     op=random.sample(new_operator,1)
#     result=" ".join(op)
#     number =result+""+str(ran)
#     print(number.replace("0","+62",1))
#     pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), pesan+"\n\n"+link, 10, tab_close=True)

# # jumlah nomer 10
# def process3(pesan,link):
#     ran=random.randint(100000, 999999)
#     op=random.sample(new_operator,1)
#     result=" ".join(op)
#     number =result+""+str(ran)
#     print(number.replace("0","+62",1))
#     pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), pesan+"\n\n"+link, 10, tab_close=True)

# # jumlah nomer 10 - 12
# def process4(pesan,link):
#     ran=random.randint(100000, 99999999)
#     op=random.sample(new_operator,1)
#     result=" ".join(op)
#     number =result+""+str(ran)
#     print(number.replace("0","+62",1))
#     pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), pesan+"\n\n"+link, 10, tab_close=True)

def loopp(kode):
    data = api(kode)
    i=1
    if(data['code']==200):
        for key in data['data']:
            while i<20:
                print("program run")
                Controller.jabodetabek(key['note'],key['link'])
                time.sleep(5)
                Controller.balinus(key['note'],key['link'])
                time.sleep(5)
                Controller.jawabarat(key['note'],key['link'])
                time.sleep(5)
                Controller.jawatengah(key['note'],key['link'])
                time.sleep(5)
                Controller.jawatimur(key['note'],key['link'])
                time.sleep(5)
                i+=1
                
        loopp(kode)   
    else:
        print("keluar dan jalankan lagi programnya")

def main():
    kode = input("Masukan Kode Di Website? = ")
    loopp(kode)
    
    

if __name__ == "__main__":
    main()