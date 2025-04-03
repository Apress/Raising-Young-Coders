import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led = True
button = False

while True:
    if (not button and GPIO.input(22)):
        led = not led
    button = GPIO.input(22)
    GPIO.output(17, led)
    GPIO.output(27, not led)
    time.sleep(0.05)