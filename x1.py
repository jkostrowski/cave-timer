from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont

import RPi.GPIO as GPIO 

import subprocess
import time


class Display(object):
  def __init__(self):
    serial = spi(device=0, port=0)
    self.device = sh1106(serial)
    self.font1 = ImageFont.truetype('fonts/DejaVuSansCondensed-Bold.ttf', 16)
    self.font2 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 12) 
    self.font3 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 8) 
    print( self.device.bounding_box )

  def demo(self):
    with canvas(self.device) as draw:
      draw.rectangle(self.device.bounding_box, outline="black", fill="black")
      draw.text((0, 0), "Out 22/10 64/10", font=self.font1, fill=255)
      draw.text((0, 24), "12|06|15|12|22|*", font=self.font2, fill=255)
      draw.text((0, 46), "JKO", font=self.font3, fill=255)

  def show(self, model):
    model.render()

    if not model.refresh:
      return 

    print( "%s - %s" % (model.time, model.message))

    with canvas(self.device) as draw:
      draw.rectangle(self.device.bounding_box, outline="black", fill="black")
      draw.text((0, 0), model.time, font=self.font1, fill=255)
      draw.text((0, 24), model.message, font=self.font2, fill=255)

  def clean(self):
    with canvas(self.device) as draw:
      draw.rectangle(self.device.bounding_box, outline="black", fill="black")


class Model:
  def __init__(self):
    self.t0 = time.monotonic()
    self.t1 = time.monotonic()
    self.time = "00:00"
    self.message = ""
    self.refresh  = True
    self.prev = ""

  def snapshot(self):
    return self.time + ':' + self.message

  def render(self):
    dt = self.t1-self.t0
    self.time = '%02d:%02d' % ( dt / 60, dt % 60)
    snap = self.snapshot()
    self.refresh = (self.prev != snap) 
    self.prev = snap


class Buttons(object):
  BUTTON1 = 21
  BUTTON2 = 20

  E_NONE = 0
  E_B1   = 1
  E_B2   = 2
  E_BOTH = 3

  def __init__(self):
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(self.BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.add_event_detect(self.BUTTON1, GPIO.RISING)
    GPIO.add_event_detect(self.BUTTON2, GPIO.RISING)

  def event(self):
    b1 = b2 = False 

    if GPIO.event_detected(self.BUTTON1):
      b1 = True
      time.sleep(.2)
      if GPIO.event_detected(self.BUTTON1):
        None

    if GPIO.event_detected(self.BUTTON2):
      b2 = True
      time.sleep(.2)
      if GPIO.event_detected(self.BUTTON2):
        None

    if b1 & b2:
      return self.E_BOTH
    elif b1:
      return self.E_B1
    elif b2: 
      return self.E_B2
    else:
      return self.E_NONE

## =================================

m = Model()
d = Display()
b = Buttons()

def update_model(event, model):
  model.t1 = time.monotonic()

  if event == Buttons.E_BOTH:
    model.message = "xx"
  elif event == Buttons.E_B1:
    model.message = "B1"
  elif event == Buttons.E_B2:
    model.message = "B2"
  else:
    model.message = ""

x = 0 
while x < 100:
  x += 1
  e = b.event()
  update_model( e, m )
  d.show( m )
  time.sleep(.1)

d.clean()
