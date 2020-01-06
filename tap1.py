from time import sleep
import board
import busio
import adafruit_lsm303_accel
import adafruit_lsm303agr_mag

i2c = busio.I2C(board.SCL, board.SDA)
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)
accel.range = adafruit_lsm303_accel.Range.RANGE_2G
accel.set_tap(1, 30)

while True:
    a = accel.acceleration
    sleep(0.5)
    if accel.tapped:
        print("Tapped!\n")
        b = accel.acceleration
        print("Delta: X=%6.2f Y=%6.2f Z=%6.2f" % (b[0]-a[0], b[1]-a[1], b[2]-a[2]))

