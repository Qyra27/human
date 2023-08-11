#main program

#import library dulu
from module.rfid_controller import * # import semua codingan dari rfid_controller
from module.ubidots_controller  import *

#challenge malam ini jadi besok pagi
'''
1. Baca RFID dulu
2. RFID yang terbaca dikirim ke Ubidots
'''

try:
        id_rfid, text_rfid = read_rfid()
        print(text_rfid)
finally:
        GPIO.cleanup()

#nambah hello world
print('Hello WOrld')
