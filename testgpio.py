#Script allows pins to go on and off to test the pins with a multimeter.
import machine
import time

# Define the pins to test
pins = [2, 3, 4, 5]

# Initialize the pins as outputs
gpio_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in pins]

while True:
    for pin in gpio_pins:
        pin.value(1)  # Set pin high
        time.sleep(0.5)
        pin.value(0)  # Set pin low
        time.sleep(0.5)
