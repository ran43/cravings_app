from PageUI import *
from tkinter import *

class AddResponseOptionsUI(PageUI):
	def __init__(self, owning_UI_manager, owning_category_UI, window):
		PageUI.__init__(self, owning_UI_manager, window=window)
		self.owning_category_ui = owning_category_UI
		self.back_button = Button(master=window, text="Back", command=self.back_button_callback)
		self.explanatory_label = Label(master=window, text = "Please select the reason\n you would like to add a response to.")
		self.recalculate_widgets_in_page()
		self.main_button = Button(master=window, text = "Add a Response", command = self.add_response_button_callback)

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = [self.explanatory_label] + [option_UI.add_response_button for option_UI in self.owning_category_ui.options_ui.option_UIs_list]
		self.widgets_in_page.append(self.back_button)

	def add_response_button_callback(self):
		self.owning_UI_manager.go_to_page(self)

	def back_button_callback(self):
		self.owning_UI_manager.go_to_page(self.owning_category_ui)

	def load_page(self):
		self.recalculate_widgets_in_page()
		PageUI.load_page(self)



