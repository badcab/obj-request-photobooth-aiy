import math
import time

from aiy.vision.leds import Leds
from aiy.vision.leds import Pattern
from aiy.vision.leds import PrivacyLed
from aiy.vision.leds import RgbLeds

class Led_module:
	RED = (0xFF, 0x00, 0x00)
	GREEN = (0x00, 0xFF, 0x00)
	YELLOW = (0xFF, 0xFF, 0x00)
	BLUE = (0x00, 0x00, 0xFF)
	PURPLE = (0xFF, 0x00, 0xFF)
	CYAN = (0x00, 0xFF, 0xFF)
	WHITE = (0xFF, 0xFF, 0xFF)
	OFF = (0x00, 0xFF, 0xFF)

	leds = Leds()

	def __init__(self, verbose):
		self.verbose = bool(verbose)

	def set_led_red(self):
		leds.update(Leds.reg_on(RED))
		if(self.verbose):
			print(__name__)

	def set_led_yellow():
		leds.update(Leds.reg_on(YELLOW))
		if(self.verbose):
			print(__name__)

	def set_led_green():
		leds.update(Leds.reg_on(GREEN))
		if(self.verbose):
			print(__name__)

	def set_led_off():
		leds.update(Leds.rgb_off())
		if(self.verbose):
			print(__name__)

	def set_privacy_on():
		leds.update(Leds.privacy_on())
		if(self.verbose):
			print(__name__)

	def set_privacy_off():
		leds.update(Leds.privacy_off())
		if(self.verbose):
			print(__name__)

	def set_led_blink():
		leds.pattern = Pattern.blink(500)
		if(self.verbose):
			p(__name__)

	def reset_led():
		leds.reset()
		if(self.verbose):
			print(__name__)
