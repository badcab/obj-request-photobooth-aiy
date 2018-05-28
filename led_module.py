class Led_module:
	from aiy.vision.leds import Leds
	from aiy.vision.leds import Pattern
	from aiy.vision.leds import PrivacyLed
	from aiy.vision.leds import RgbLeds

	RED = (0xFF, 0x00, 0x00)
	GREEN = (0x00, 0xFF, 0x00)
	YELLOW = (0xFF, 0xFF, 0x00)
	BLUE = (0x00, 0x00, 0xFF)
	PURPLE = (0xFF, 0x00, 0xFF)
	CYAN = (0x00, 0xFF, 0xFF)
	WHITE = (0xFF, 0xFF, 0xFF)
	OFF = (0x00, 0xFF, 0xFF)

	leds = Leds()

	def set_led_red(self):
		self.leds.update(self.Leds.rgb_on(self.RED))

	def set_led_yellow(self):
		self.leds.update(self.Leds.rgb_on(self.YELLOW))

	def set_led_green(self):
		self.leds.update(self.Leds.rgb_on(self.GREEN))

	def set_led_off(self):
		self.leds.update(self.Leds.rgb_off())

	def set_privacy_on(self):
		self.leds.update(self.Leds.privacy_on())

	def set_privacy_off(self):
		self.leds.update(self.Leds.privacy_off())

	def set_led_blink(self):
		self.leds.pattern = self.Pattern.blink(500)

	def reset_led(self):
		self.leds.reset()
