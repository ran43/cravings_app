from PageUI import *

class HistoryUI(PageUI):
	def __init__(self, owning_UI_manager, window, owning_category_UI):
		PageUI.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.owning_category_UI=owning_category_UI
	