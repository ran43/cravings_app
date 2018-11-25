from UIClass import *
from tkinter import *

class ResponseUI(UIClass):
	def __init__(self, owning_UI_manager, label, window, response):
		UIClass.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.label = label
		self.display_label = Button(master=window, text=label)
		self.main_button = Button(master=window, text=label)
		self.corresponding_response = response
		