import board
import busio
import adafruit_lsm303_accel
import adafruit_lsm303agr_mag

i2c = busio.I2C(board.SCL, board.SDA)
mag = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)

print("Acceleration (m/s^2): X=%0.3f Y=%0.3f Z=%0.3f"%accel.acceleration)
print("Magnetometer (micro-Teslas)): X=%0.3f Y=%0.3f Z=%0.3f"%mag.magnetic)


