import time 
import board
import busio
import adafruit_lsm303_accel
import adafruit_lsm303agr_mag

i2c = busio.I2C(board.SCL, board.SDA)
mag = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)

q = 30

pastx = []
pasty = []
pastz = []

sumx = 0
sumy = 0
sumz = 0

while len(pastx) < q:
    a = accel.acceleration
    pastx.append(a[0])
    pasty.append(a[1])
    pastz.append(a[2])
    sumx += a[0]
    sumy += a[1]
    sumz += a[2]

while True:
    a = accel.acceleration
    data = (a[0], a[1], a[2], sumx/q, sumy/q, sumz/q, a[0] - sumx/q, a[1] - sumy/q, a[2] - sumz/q)
    if max(abs(data[6]), abs(data[7]), abs(data[8])) > 0:
       print("Acceleration (m/s^2): X=%3.0f Y=%3.0f Z=%3.0f | ax=%3.0f ay=%3.0f az=%3.0f | dx=%3.0f dy=%3.0f dz=%3.0f" % data)
    # print("Magnetometer (micro-Teslas)): X=%0.3f Y=%0.3f Z=%0.3f"%mag.magnetic)
    sumx += a[0] - pastx[0]
    sumy += a[1] - pasty[0]
    sumz += a[2] - pastz[0]
    pastx.pop(0)
    pasty.pop(0)
    pastz.pop(0)
    pastx.append(a[0])
    pasty.append(a[1])
    pastz.append(a[2])
    time.sleep(0.1)


