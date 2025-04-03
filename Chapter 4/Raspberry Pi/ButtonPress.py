import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.output(17, GPIO.input(22))
    time.sleep(0.05)