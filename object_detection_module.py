class Object_detection_module:

	import argparse
	import io
	import sys
	from PIL import Image
	from PIL import ImageDraw

	from aiy.vision.inference import ImageInference
	from aiy.vision.models import object_detection
	
	def _crop_center(self, image): #@TODO remove depencancy on this
		width, height = image.size
		size = min(width, height)
		x, y = (width - size) / 2, (height - size) / 2
		return image.crop((x, y, x + size, y + size)), (x, y)

	def get_on_screen(self):
		with ImageInference(object_detection.model()) as inference:
			image = Image.open(
				io.BytesIO(sys.stdin.buffer.read())
				if args.input == '-' else args.input)
			image_center, offset = self._crop_center(image)
			draw = ImageDraw.Draw(image)
			result = inference.run(image_center)
			for i, obj in enumerate(object_detection.get_objects(result, 0.3, offset)):
				print('Object #%d: %s' % (i, str(obj)))
			
			return ['banana', 'face'] #@TODO make this actually work


#goal is to just get a list of things on the screen