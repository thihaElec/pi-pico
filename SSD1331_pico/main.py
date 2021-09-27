from machine import Pin, SPI
import ssd1331
import framebuf
import utime
import math


# spi initialisation
spi = SPI(0,baudrate=6000000,sck=Pin(6),mosi=Pin(7))
dc=Pin(8,Pin.OUT)
cs=Pin(9,Pin.OUT)

# oled initialisation
width=96
height=64
oled = ssd1331.SSD1331(spi=spi,dc=Pin(8),cs=Pin(9),width=width, height=height)
oled.fill(0)

while True:
    temp=2234.5
    oled.putText(20,20,str(temp),0xffff)