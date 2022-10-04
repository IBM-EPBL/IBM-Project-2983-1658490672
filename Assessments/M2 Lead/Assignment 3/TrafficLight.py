import time
from machine import Pin

Red_Pin = 15
yellow_Pin = 2
green_pin = 4

Red_led=Pin(Red_Pin,Pin.OUT) 
yellow_led=Pin(yellow_Pin,Pin.OUT) 
green_led=Pin(green_pin,Pin.OUT)

while True:
  Red_led.value(1)        
  time.sleep(5)
  Red_led.value(0)

  yellow_led.value(1)           
  time.sleep(3)
  yellow_led.value(0)

  green_led.value(1)
  time.sleep(5)
  green_led.value(0)
