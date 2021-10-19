#!/usr/bin/python37all

import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led1 = 16
led2 = 20
led3 = 21

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

pwm1 = GPIO.PWM(led1, 100)
pwm1.start(0)

pwm2 = GPIO.PWM(led2, 100)
pwm2.start(0)

pwm3 = GPIO.PWM(led3, 100)
pwm3.start(0)

while True:
  with open('selected_led.txt', 'r') as f:
    data = json.load(f)
  dutyCycle = float(data['slider'])

  if (data['option']==1):
    pwm1.ChangeDutyCycle(dutyCycle)
  elif (data['option']==2):
    pwm2.ChangeDutyCycle(dutyCycle)
  elif (data['option']==3):
    pwm3.ChangeDutyCycle(dutyCycle)
  time.sleep(.1)


  





