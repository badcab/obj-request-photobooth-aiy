#pic a rondom object or 2 and a quantity of people
#trigger camera when that condition is met

#for starters let us trigger a picture based on a static requirment
import time
import led_module
import sound_module

def main():
	lights = led_module.Led_module()
	sound = sound_module.Sound_module()
	detect = object_detection_module.Object_detection_module()
	req = rand_photo_requirements.Rand_photo_req()

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
	

	while 1 == 1: #@TODO change to while btn not pressed
		requirement = req.get_new_photo_requirement()
		while requirement != detect.get_on_screen(): #@TODO change to be contains
			print('====================================================')
			time.sleep(1) #slows things down a bit
			#determine the color of the led
		#end while
		lights.set_led_green()
		lights.set_led_blink()
		#take the actual picture here
		sound.shutter()
		#move picture to target directory
	#end while
	#take the actual picture
	sound.shutter()
	#move picture to target directory
	main() #recursively call function again to resume


if __name__ == '__main__':
	main()