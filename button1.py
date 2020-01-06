from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# prev = False  

while True: # Run forever
    sleep(0.1)
    if GPIO.input(10) == GPIO.LOW:
        print("Button was pushed!")


