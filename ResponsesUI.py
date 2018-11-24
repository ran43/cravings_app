from PageUI import *
from tkinter import *

class ResponsesUI(PageUI):
	def __init__(self, owning_UI_manager, window, owning_category_UI):
		PageUI.__init__(self, owning_UI_manager, window=window)
		self.response_UIs_to_load = []
		self.done_button = Button(master=window, text='Done',command=self.done_button_callback)
		self.back_button = Button(master=window, text='Back', command=self.back_button_callback)
		self.recalculate_widgets_in_page()
		self.response_UIs_list = []
		self.owning_category_UI = owning_category_UI

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = [response_UI.main_button for response_UI in self.response_UIs_to_load]
		self.widgets_in_page += [self.done_button, self.back_button]

	def back_button_callback(self):
		self.owning_UI_manager.go_to_page(self.owning_category_UI.options_ui)

	def done_button_callback(self):
		self.increment_displayed_response_denominators()
		self.increment_selected_response_numerators()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)

	def increment_displayed_response_denominators(self):
		# Wants moving to the Responses.py class.
		pass

	def increment_selected_response_numerators(self):
		# Wants moving to the Responses.py class.
		pass
