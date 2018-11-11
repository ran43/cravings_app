from tkinter import *
from UIClass import * 

class PageUI(UIClass):
	def __init__(self, owning_UI_manager, window):
		UIClass.__init__(self,owning_UI_manager=owning_UI_manager, window=window)
		self.widgets_in_page = []

	def load_page(self):
		number_of_widgets = len(self.widgets_in_page)
		rely_base_constant = 1.0 / (number_of_widgets + 1)
		relheight_base_expression = 0.75 * rely_base_constant
		for index, widget in enumerate(self.widgets_in_page):
			if isinstance(widget, Button):
				self.display_button(button=widget,rely=rely_base_constant * (1 + index), relheight = relheight_base_expression)
			elif isinstance(widget, Label):
				self.display_label(label=widget,rely=rely_base_constant * (1 + index), relheight = relheight_base_expression)
			self.owning_UI_manager.widgets_loaded.append(widget)
