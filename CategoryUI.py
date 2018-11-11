from tkinter import *
from PageUI import *
from OptionsUI import *
from ResponsesUI import *
from TimerUI import *
from AchievementsUI import *
from StatsUI import *
from HistoryUI import *

class CategoryUI(PageUI):
	def __init__(self, owning_UI_manager, category, window):
		"""Takes the UI it is owned by as an argument and the category it is representing."""
		PageUI.__init__(self, window = window, owning_UI_manager=owning_UI_manager)
		self.options_ui = OptionsUI(owning_UI_manager=owning_UI_manager, owning_category_UI=self, window=window)
		self.responses_ui = ResponsesUI(owning_UI_manager=owning_UI_manager, window=window)
		self.timer_ui = TimerUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.achievements_ui = AchievementsUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.history_ui = HistoryUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.stats_ui = StatsUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.category_represented = category
		self.main_button = Button(window, text=category.name) # Need to add the command later.


