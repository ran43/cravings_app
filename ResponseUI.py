from UIClass import *
from tkinter import *

class ResponseUI(UIClass):
	def __init__(self, owning_UI_manager, label, window, response):
		UIClass.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.label = label
		self.display_label = Button(master=window, text=label)
		self.main_button = Button(master=window, text=label, highlightbackground='blue', command=lambda: self.main_button_toggle(self.main_button))
		self.corresponding_response = response

	def main_button_toggle(self, button):
		if self.corresponding_response.selected == False:
			self.press_button(button)
			self.corresponding_response.times_pressed += 1
		else:
			self.unpress_button(button)
			self.corresponding_response.times_pressed -= 1

	def press_button(self, button):
		button.config(highlightbackground='green')
		self.corresponding_response.selected = True

	def unpress_button(self, button):
		button.config(highlightbackground='blue')
		self.corresponding_response.selected=False	

		