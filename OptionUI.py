from UIClass import *
from tkinter import *

class OptionUI(UIClass):
	def __init__(self, owning_UI_manager, window, label, option):
		UIClass.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.main_button = Button(master=window, text=label)
		self.corresponding_option=option

		