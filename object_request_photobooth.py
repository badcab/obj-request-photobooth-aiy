#pic a rondom object or 2 and a quantity of people
#trigger camera when that condition is met

#for starters let us trigger a picture based on a static requirment

import led_module

def main():
	lights = led_module.Led_module(1)

	lights.set_led_red()
	sleep(5)



if __name__ == '__main__':
	main()