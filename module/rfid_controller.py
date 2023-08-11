#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.cleanup()
reader = SimpleMFRC522()

#fungsi membaca rfid
def read_rfid():
        '''
        Fungsi ini berguna untuk membaca RFID,
        tag RFID yang terbaca akan dikembalikan / return
        '''
        id, text = reader.read()
        return id,text

def write_rfid(name):
         print("Now place your tag to write")
         reader.write(name)
         print(f"{name} Written")

'''
#contoh penggunaan code
write_rfid(name='Farid al hisni') #ini tu mau nulis Ilham

#delay 3 detik
time.sleep(3)

try:
        id_rfid, text_rfid = read_rfid()
        print(text_rfid)
finally:
        GPIO.cleanup()
'''
