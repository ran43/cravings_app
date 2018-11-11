from UIClass import *

class TimerUI(UIClass):
	def __init__(self, owning_UI_manager, owning_category_UI, window):
		UIClass.__init__(self, owning_UI_manager,window=window)
		self.owning_category_UI=owning_category_UI