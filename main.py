
import imp
import random
import string
import numpy as np
import pywhatkit
import requests
import time
from controller.XlController import Controller
from controller.SmartfrenController import ControllerSmartfren
from controller.TelkomselController import TelkomselController
 
    
def api(kode):
    API_ENDPOINT = "https://tokopedia.kedaiwoeloeng.com/api/affiliate"
  
    # data to be sent to api
    data = {'kode':kode}
    
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)
    
    # extracting response text 
    result = r.json()
    return result

def loopp(kode):
    data = api(kode)
    if(data['code']==200):
        for key in data['data']:
                print(key['name'])
                print("====================")
                ControllerSmartfren.default(key['note'],key['link'],key['name'])
                time.sleep(5)
                ControllerSmartfren.jabodetabek(key['note'],key['link'],key['name'])
                time.sleep(5)
                ControllerSmartfren.jateng(key['note'],key['link'],key['name'])
                time.sleep(5)
                TelkomselController.jawatimur(key['note'],key['link'],key['name'])
                time.sleep(5)
                TelkomselController.sumatera(key['note'],key['link'],key['name'])
                time.sleep(5)
                Controller.jabodetabek(key['note'],key['link'],key['name'])
                time.sleep(5)
                Controller.balinus(key['note'],key['link'],key['name'])
                time.sleep(5)
                Controller.jawabarat(key['note'],key['link'],key['name'])
                time.sleep(5)
                Controller.jawatengah(key['note'],key['link'],key['name'])
                time.sleep(5)
                Controller.jawatimur(key['note'],key['link'],key['name'])
                time.sleep(5)
                
        nexts(kode)   
    else:
        print("keluar dan jalankan lagi programnya")

def nexts(kode):
    loopp(kode)

def main():
    kode = input("Masukan Kode Di Website? = ")
    loopp(kode)
    
    

if __name__ == "__main__":
    main()