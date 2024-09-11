import RPi.GPIO as GPIO
from hx711 import HX711

# Set up HX711
hx = HX711(dout_pin=17, pd_sck_pin=27)  # Use the GPIO pins connected to DT and SCK
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
hx.tare()  # Tare to zero out the scale

try:
    while True:
        val = hx.get_weight(5)
        print("Weight:", val)
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()