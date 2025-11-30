

from machine import Pin
import time

# Onboard LED pin (Pico W uses GP25)
led = Pin(25, Pin.OUT)

print("I am version 2.0.0")

print("Starting LED blink program...")

range _ in range(2):
    led.value(1)  # LED ON
    time.sleep(0.5)
    led.value(0)  # LED OFF
    time.sleep(0.5)
