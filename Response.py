
#Response
class Response():
	def __init__(self, owner, label):
		self.name = label
		self.owner = owner
		self.selected = False
		self.times_shown = 0.0
		self.times_pressed = 0.0
		self.selected = False