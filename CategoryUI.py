from tkinter import *
from PageUI import *
from OptionsUI import *
from ResponsesUI import *
from TimerUI import *
from AchievementsUI import *
from StatsUI import *
from HistoryUI import *
from AddResponsesOptionsUI import *

class CategoryUI(PageUI):
	def __init__(self, owning_UI_manager, category, window, owning_category_manager):
		"""Takes the UI it is owned by as an argument and the category it is representing."""
		PageUI.__init__(self, window = window, owning_UI_manager=owning_UI_manager)
		self.category_represented = category
		self.owning_category_manager=owning_category_manager
		self.options_ui = OptionsUI(owning_UI_manager=owning_UI_manager, owning_category_UI=self, window=window)
		self.responses_ui = ResponsesUI(owning_UI_manager=owning_UI_manager, window=window, owning_category_UI=self)
		self.timer_ui = TimerUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window, equivalent_timer=self.category_represented.timer)
		self.achievements_ui = AchievementsUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.history_ui = HistoryUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.stats_ui = StatsUI(owning_category_UI=self, owning_UI_manager=owning_UI_manager, window=window)
		self.main_button = Button(window, text=category.name, command=self.main_button_callback)
		self.back_button = Button(master=window, text="Back", command=self.back_button_callback)
		self.add_responses_ui = AddResponseOptionsUI(owning_UI_manager=owning_UI_manager, owning_category_UI=self, window=window)
		self.recalculate_widgets_in_page()


	def back_button_callback(self):
		self.owning_UI_manager.go_to_page(self.owning_category_manager)

	def main_button_callback(self):
		self.owning_UI_manager.go_to_page(self)

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = []
		if self.timer_ui.equivalent_timer.running == True:
			self.widgets_in_page = [self.timer_ui.time_elapsed_label, 
									self.timer_ui.update_timer_button,
									self.options_ui.main_button,
									self.timer_ui.stop_timer_button,
									self.stats_ui.main_button,
									self.history_ui.main_button,
									self.add_responses_ui.main_button,
									self.back_button]

		else:
			self.widgets_in_page = [self.timer_ui.start_timer_button,
									self.stats_ui.main_button,
									self.history_ui.main_button,
									self.add_responses_ui.main_button,
									self.back_button]

	def load_page(self):
		self.recalculate_widgets_in_page()
		PageUI.load_page(self)


