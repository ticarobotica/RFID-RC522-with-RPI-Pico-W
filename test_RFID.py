from machine import Pin, SoftI2C

import utime
import mfrc522
import ssd1306


lista_carduri={
    "652431761":"persoana A",
    "476800755":"persoana B",
    "1837604169":"persoana C",
    "2484075731":"persoana P1",
    "1386544579":"persoana P2"
    }

i2c=SoftI2C(sda=Pin(2), scl=Pin(3), freq=100000)
oled=ssd1306.SSD1306_I2C(128, 64, i2c)


cititor=mfrc522.MFRC522(sck=6, mosi=7, miso=4, rst=22, cs=5,spi_id=0)
print("Cititor in derulare !")
oled.text("   Cititor ",1,1)
oled.text(" in derulare",1,10)
oled.show()
while True:
    cititor.init() # initializam cititorul RFID
    (stat, tip_cititor)=cititor.request(cititor.REQIDL)
    if stat==cititor.OK:
        (stat, uid)=cititor.SelectTagSN()
        nr_card=int.from_bytes(bytes(uid),"little",False)
        print("Numar card = ",nr_card)
        oled.text("     ID-card",1,20)
        oled.text("   "+str(nr_card),1,30)
        if str(nr_card) in lista_carduri.keys():
            oled.text("   "+lista_carduri.get(str(nr_card)),1,40)
        else:
            oled.text("    Persoana",1,40)
            oled.text("neinregistrata",1,50)
            
        oled.show()
    utime.sleep_ms(1000)
    oled.fill(0)

