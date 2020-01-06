import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# font = ImageFont.load_default()
font = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 16)
print("screen height: %d, font height: %d "%(disp.height, font.getsize("2")[1]))

draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, top+0), "I:22/00:64/00", font=font, fill=255)
draw.text((x, top+18), "12|06|15|12|*", font=font, fill=255)

disp.image(image)
disp.show()

sleep( 10 )

# Clear display.
disp.fill(0)
disp.show()

