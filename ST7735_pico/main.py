import time
import lcd_gfx
from bmp import bmp
from machine import Pin, SPI
import ST7735

spi = machine.SPI(0, baudrate=8000000, sck=Pin(2),mosi=Pin(3), polarity=0, phase=0)

d = ST7735.ST7735(spi=spi, rst=19, ce=20, dc=18)
d.reset()
d.begin()
d._bground = 0xffff
d.fill_screen(d._bground)

d.set_rotation(0)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(1)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(2)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(3)
bmp('flower64x48.bmp',d,10,10,1)

d._color = 0
d.set_rotation(0)
d.p_string(10,10,'Hello World')

d._color = 0xf100
d.set_rotation(1)
d.p_string(10,10,'Hello World')

d._color = 0x07e0
d.set_rotation(2)
d.p_string(10,10,'Hello World')

d._color = 0x001f
d.set_rotation(3)
d.p_string(10,10,'Hello World')

time.sleep(5)
d.set_rotation(3)
bmp('flower160x128.bmp',d,0,0,1)

time.sleep(3)
x = int(d._width/2)
y = int(d._height/2)
r = int(min(x,y)/2)
d.fill_screen(d.rgb_to_565(255,255,255))
color = d.rgb_to_565(0,36,125)
#print(x,y,color)
lcd_gfx.drawfillCircle(x,y,r,d,color)
r = int(r*2/3)
color = d.rgb_to_565(255,255,255)
lcd_gfx.drawfillCircle(x,y,r,d,color)
r = int(r/2)
color = d.rgb_to_565(206,17,38)
lcd_gfx.drawfillCircle(x,y,r,d,color)

time.sleep(3)
color = d.rgb_to_565(206,17,38)
lcd_gfx.drawRect(10,10,d._width-20,d._height-20,d,color)