from PageUI import *

class OptionsUI(PageUI):
	def __init__(self, owning_category_UI, owning_UI_manager, window):
		PageUI.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.option_UIs_list = []
		self.owning_category_UI = owning_category_UI
		self.main_button = Button(master=window, text="Craving") # Need to add a callback to this. 
		self.window = window

	def display_craving_button(self, rely, relheight):
		self.display_button(rely=rely, relheight=rely)



		