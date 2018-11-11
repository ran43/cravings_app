from Category.py import *

# CategoryList class definition
class CategoryManager():
	"""Contains a list of all of the existing categories. Also has functions to add and delete categories."""
	def __init__(self):
		self.category_list = []

	def add_category(self, new_category_name):
		new_category = Category(label=new_category_name, window=window, category_manager=self)
		self.category_list.append(new_category)
		return new_category

	def delete_category(self):
		pass
		

