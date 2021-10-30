#code ref: https://github.com/kfricke/micropython-nunchuck

from machine import I2C, SPI, Pin
import time
import pcd8544_fb
import nunchuck
import utime

nun = nunchuck.Nunchuck(I2C(0,scl=machine.Pin(17),sda=machine.Pin(16),freq=100000))
spi = SPI(0)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(5)
dc = Pin(4)
rst = Pin(8)

# if your pcd8544 has BL pin, uncomment this line.
bl = Pin(28, Pin.OUT, value=1)

lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)
import framebuf
buffer = bytearray((pcd8544_fb.HEIGHT // 8) * pcd8544_fb.WIDTH)
framebuf = framebuf.FrameBuffer(buffer, pcd8544_fb.WIDTH, pcd8544_fb.HEIGHT, framebuf.MONO_VLSB)

framebuf.fill(0)
lcd.data(buffer)
utime.sleep(1)

prex = 42
prey = 24
x = 42
y = 24

framebuf.fill_rect(x-2, y-2, 4, 4, 1) #frame size (84x48)
lcd.data(buffer)
time.sleep_ms(30)

while True:
    if not nun.joystick_center():
        if nun.joystick_up():
            y -= 5
        elif nun.joystick_down():
            y += 5
        if nun.joystick_left():
            x -= 5
        elif nun.joystick_right():
            x += 5
    #print(x, y, nun.joystick_x(), nun.joystick_y())
    if x>80:
        x=80
    if y>44:
        y=44
    if x<2:
        x=2
    if y<2:
        y=2

    j = nun.joystick()
    a = nun.accelerator()
    b = nun.buttons()
    #curx = round((j[0]*84)/255)
    #cury = round((j[1]*48)/255)
    #print(j[0],j[1],curx,cury,x,y)
    #print(x,y)
    
    if prex != x or prey != y:
        framebuf.fill_rect(prex-2, prey-2, 4, 4, 0) #removing previous cursor
        lcd.data(buffer)
        time.sleep_ms(10)
        
        framebuf.fill_rect(x-2, y-2, 4, 4, 1) #frame size (84x48)
        lcd.data(buffer)

    prex = x #curx
    prey = y #cury

    time.sleep_ms(1)
