from time import sleep
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from PIL import ImageFont

# GPIO.setwarnings(False)

serial = spi(device=0, port=0)
device = sh1106(serial)

font1 = ImageFont.truetype('fonts/DejaVuSansCondensed-Bold.ttf', 16)
font2 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 12) 
font3 = ImageFont.truetype('fonts/DejaVuSansMono.ttf', 8) 

with canvas(device) as draw:
    # draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((0, 0), "Out 22/10 64/10", font=font1, fill=255)
    draw.text((0, 24), "12|06|15|12|22|*", font=font2, fill=255)
    draw.text((0, 46), "JKO", font=font3, fill=255)
 
sleep(8)



