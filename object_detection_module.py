class Object_detection_module:
	from picamera import PiCamera
	from aiy.vision.inference import ImageInference
	from aiy.vision.models import object_detection

	def get_on_screen(self):
		with self.PiCamera() as camera:
			camera.sensor_mode = 4
			camera.resolution = (1640, 922)  #  1232 is Full height (Camera v2), 922 is 16:9 
			camera.framerate = 30

			with self.CameraInference(self.object_detection.model()) as inference:
				result = inference.run()
				for i, obj in enumerate(object_detection.get_objects(result, 0.3)):
					print('Object #%d: %s' % (i, str(obj)))

				camera.stop_preview() #to clean it up
				return ['banana', 'face'] #@TODO make this actually work


#goal is to just get a list of things on the screen