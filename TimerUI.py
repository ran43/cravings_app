from UIClass import *
from tkinter import *

class TimerUI(UIClass):
	def __init__(self, owning_UI_manager, owning_category_UI, window, equivalent_timer):
		UIClass.__init__(self, owning_UI_manager,window=window)
		self.owning_category_UI = owning_category_UI
		self.equivalent_timer = equivalent_timer
		self.time_elapsed_label = Label(master=window, text="{} days, {} hours, {} minutes, {} seconds".format(*self.equivalent_timer.formatted_time_elapsed))
		self.start_timer_button = Button(master=window, text="Start Timer", command=self.start_timer_button_callback)
		self.update_timer_button = Button(master=window, text="Update Timer")
		self.stop_timer_button = Button(master=window, text = "Streak Broken")

	def start_timer_button_callback(self):
		self.equivalent_timer.start_timer()
		self.owning_category_UI.recalculate_widgets_in_page()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)