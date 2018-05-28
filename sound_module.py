class Sound_module:
	import aiy.toneplayer

	def shutter(self): #@TODO make a camera sound
		ts = [
			'E5q',
			'Be',
			'C5e',
		]
		player = self.aiy.toneplayer.TonePlayer(22)
		player.play(*ts)

	def blip(self): #@TODO make a blip sound
		ts = [
			'E5q',
			'C5q',
			'Aq',
			'Aq',
		]
		player = self.aiy.toneplayer.TonePlayer(22)
		player.play(*ts)

#@TODO auto implament class when importing