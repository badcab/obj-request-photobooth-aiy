#pic a rondom object or 2 and a quantity of people
#trigger camera when that condition is met

#for starters let us trigger a picture based on a static requirment
import time
import led_module
import sound_module

def main():
	lights = led_module.Led_module()
	sound = sound_module.Sound_module()

	sound.shutter()
	lights.set_led_red()
	time.sleep(1)
	lights.set_led_yellow() #@todo yellow look a little green
	time.sleep(1)
	lights.set_led_green()
	time.sleep(1)
	lights.set_led_blink() #@TODO blink is currently broken
	time.sleep(1)
	lights.set_led_off()
	sound.blip()


if __name__ == '__main__':
	main()