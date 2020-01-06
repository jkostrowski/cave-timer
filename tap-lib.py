import time
import board
import busio
import subprocess
import adafruit_lsm303_accel
import adafruit_lsm303agr_mag
import adafruit_ssd1306

from PIL import Image, ImageDraw, ImageFont


i2c   = busio.I2C(board.SCL, board.SDA)
mag   = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)
acc   = adafruit_lsm303_accel.LSM303_Accel(i2c)
disp  = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

acc.data_rate = adafruit_lsm303_accel.Rate.RATE_100_HZ
acc.range     = adafruit_lsm303_accel.Range.RANGE_2G
acc.mode      = adafruit_lsm303_accel.Mode.MODE_HIGH_RESOLUTION

acc.set_tap(1, 40, time_limit=10, time_latency=20, time_window=255)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
width  = disp.width
height = disp.height
image  = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# font = ImageFont.load_default()
font = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 16)

def oled(txt):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), txt, font=font, fill=255)
    disp.image(image)
    disp.show()


oled("Sensing")

while True:
    x = acc.acceleration[0]
    txt = ""
    if acc.tapped:
        tap = True
        txt += "TAP"
        oled("===Tap===")
    else:
        oled("")

    data = (x, txt)
    print("x=%6.2f | %s" % data)
    time.sleep(0.01)





