from tkinter import *
from PageUI.py import *

class CategoryUI(PageUI):
	def __init__(self, owning_UI_manager, category):
		"""Takes the UI it is owned by as an argument and the category it is representing."""
		self.PageUI.__init__(self, owning_UI_manager=owning_UI_manager)
		self.options_ui = OptionsUI()
		self.responses_ui = ResponsesUI()
		self.timer_ui = TimerUI()
		self.achievements_ui = AchievementsUI()
		self.history_ui = HistoryUI()
		self.stats_ui = StatsUI()
		self.category_represented = category
		self.main_button = Button(window, text=category.name) # Need to add the command later.


