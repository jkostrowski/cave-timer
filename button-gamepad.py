import gamepad
import board

B1 = 1 << 0
B2 = 1 << 1

pad = gamepad.GamePad(
    digitalio.DigitalInOut(board.D21),
    digitalio.DigitalInOut(board.D20),
)

while True:
    buttons = pad.get_pressed()
    if buttons & B1:
        print("B1")
    elif buttons & B2:
        print("B2")
    time.sleep(0.1)
    while buttons:
        buttons = pad.get_pressed()
        time.sleep(0.1)
