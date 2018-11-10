
#Response
class Response():
	def __init__(self, owner, label):
		self.name = label
		self.counter = 0
		self.owner = owner
		self.selected = False

	def select_response(self):
		self.selected = True