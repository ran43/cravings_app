from PageUI.py import *

class OptionsUI(PageUI):
	def __init__(self, owning_category_UI, owning_UI_manager):
		self.PageUI.__init__(self, owning_UI_manager=owning_UI_manager)
		self.option_UIs_list = []
		self.owning_category_UI = owning_category_UI
		self.main_button = Button(window=window, text="Craving") # Need to add a callback to this. 

	def display_craving_button(self, rely, relheight):
		self.display_button(rely=rely, relheight=rely)



		