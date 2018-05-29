class Photo_module:
	import datetime
	
	def take_photo(self):
		#take picture of whatever is on the screen
		
	def move_photo(self):
		#this will handle the moving to the remote web server
		
	def get_photo_name(self, append = []):
		s = now.strftime("%Y-%b-%d_%H-%M-%S")
		if(len(append)):
			s = s + '-'.join(append)
		return s + '.png'