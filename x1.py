from time import sleep
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess


class Display(object):
  def init(self):
    serial = spi(device=0, port=0)
    self.device = sh1106(serial)
    self.font1 = ImageFont.truetype('fonts/DejaVuSansCondensed-Bold.ttf', 16)
    self.font2 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 12) 
    self.font3 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 8) 

  def showTimers(self):
    with canvas(self.device) as draw:
      draw.rectangle(self.device.bounding_box, outline="black", fill="black")
      draw.text((0, 0), "Out 22/10 64/10", font=self.font1, fill=255)
      draw.text((0, 24), "12|06|15|12|22|*", font=self.font2, fill=255)
      draw.text((0, 46), "JKO", font=self.font3, fill=255)

  def clean(self):
    with canvas(self.device) as draw:
      draw.rectangle(self.device.bounding_box, outline="black", fill="black")



def initButtons():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


#initButtons()

oled = Display()
oled.init()
oled.showTimers()
sleep(2)
oled.clean()

#while True: # Run forever
#    sleep(0.1)
#    if GPIO.input(10) == GPIO.LOW:
#        print("Button was pushed!")


