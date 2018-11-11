from PageUI import *

class StatsUI(PageUI):
	def __init__(self, owning_UI_manager, owning_category_UI, window):
		PageUI.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.owning_category_UI = owning_category_UI
		self.main_button = Button(master=window, text="Stats")