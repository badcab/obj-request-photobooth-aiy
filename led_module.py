import math
import time

from aiy.leds import Leds
from aiy.leds import Pattern
from aiy.leds import PrivacyLed
from aiy.leds import RgbLeds

RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
YELLOW = (0xFF, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)
PURPLE = (0xFF, 0x00, 0xFF)
CYAN = (0x00, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)
OFF = (0x00, 0xFF, 0xFF)

leds = Leds()

def set_led_red
	leds.update(Leds.reg_on(RED))
	
def set_led_yellow
	leds.update(Leds.reg_on(YELLOW))
	
def set_led_green
	leds.update(Leds.reg_on(GREEN))
	
def set_led_off
	leds.update(Leds.rgb_off())
	
def set_privacy_on
	leds.update(Leds.privacy_on())

def set_privacy_off
	leds.update(Leds.privacy_off())
	
def set_led_blink
	leds.pattern = Pattern.blink(500)
	
def reset_led
	leds.reset()