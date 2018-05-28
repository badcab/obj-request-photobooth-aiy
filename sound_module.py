class Sound_module:
	import aiy.toneplayer

	def shutter(self):
		ts = [
			'E5q',
			'Be',
			'C5e',
		]
		player = aiy.toneplayer.TonePlayer(22)
		player.play(*ts)