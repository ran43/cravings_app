from UIClass import *
from tkinter import *

class OptionUI(UIClass):
	def __init__(self, owning_UI_manager, window, label, option, owning_options_UI):
		UIClass.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.main_button = Button(master=window, text=label, highlightbackground='blue', command=lambda: self.toggle(self.main_button))
		self.corresponding_option=option
		self.owning_options_UI=owning_options_UI
		# This is the option button that appears on the AddResponsesUI page and when pressed it will go to a page displaying all the responses for this option and will give you the opportunity to add a response.
		self.add_response_button = Button(master=window, text=label, command=self.add_response_button_callback)
		self.add_response_display_responses_ui = 

	def toggle(self, button):
		if self.corresponding_option.selected == False and self.corresponding_option.owning_category.total_selected <= 5:
			self.press_button(button)
			self.corresponding_option.owning_category.total_selected+=1
		else:
			self.unpress_button(button)
			self.corresponding_option.owning_category.total_selected-=1


	def press_button(self, button):
		button.config(highlightbackground='green')
		if self.corresponding_option.selected == False:
			self.corresponding_option.owning_category.total_selected+=1
		self.corresponding_option.selected = True

	def unpress_button(self, button):
		button.config(highlightbackground='blue')
		if self.corresponding_option.selected == True:
			self.corresponding_option.owning_category.total_selected-=1
		self.corresponding_option.selected=False	

	def add_response_button_callback(self):
		self.owning_UI_manager.go_to_page(self.add_response_display_responses_ui)





		