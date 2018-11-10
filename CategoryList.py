# CategoryList class definition
class CategoryList():
	"""Contains the list of all the categories as a list. Also has functions to """
	def __init__(self):
		self.category_list = []

	def undisplay_categories(self):
		for category in self.category_list:
			category.category_button.place_forget()

	def load_categories_page(self):
		self.display_categories()
		self.display_add_category_button()
		self.display_delete_category_button()

	def display_categories(self):
		for index, category in enumerate(self.category_list):
			category.display_category_button((index+1.0)/(4+len(self.category_list)), (3.0/4.0)/(len(self.category_list)+4.0))
			

	def display_add_category_button(self):
		pass

	def display_delete_category_button(self):
		pass