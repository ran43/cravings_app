# Option
class Option():
	def __init__(self, label, owner):
		self.name = label
		self.responses_list = []
		self.counter = 0
		self.selected = False
		self.owning_category = owner

	def add_response(self):
		pass

	def delete_response(self):
		pass