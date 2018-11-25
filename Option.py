from Response import *
from LoadSaveData import *

class Option():
	def __init__(self, label, owner):
		self.name = label
		self.responses_list = []
		self.counter = 0
		self.selected = False
		self.owning_category = owner

	def add_response(self, text):
		new_response = Response(owner=self, label=text)
		self.responses_list.append(new_response)
		collect_and_save_data(self.owning_category.owner)
		return new_response

	def delete_response(self):
		pass