from UIClass import *
from tkinter import *

class TimerUI(UIClass):
	def __init__(self, owning_UI_manager, owning_category_UI, window, equivalent_timer):
		UIClass.__init__(self, owning_UI_manager,window=window)
		self.owning_category_UI = owning_category_UI
		self.equivalent_timer = equivalent_timer
		self.time_elapsed_label = Label(master=window, text="")
		self.update_time_elapsed_label()
		self.start_timer_button = Button(master=window, text="Start Timer", command=self.start_timer_button_callback)
		self.update_timer_button = Button(master=window, text="Update Timer", command=self.update_timer_button_callback)
		self.stop_timer_button = Button(master=window, text = "Streak Broken", command=self.stop_timer_button_callback)

	def start_timer_button_callback(self):
		self.equivalent_timer.start_timer()
		self.update_time_elapsed_label()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)

	def update_timer_button_callback(self):
		self.equivalent_timer.update_timer()
		self.update_time_elapsed_label()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)

	def update_time_elapsed_label(self):
		self.time_elapsed_label.configure(text="{} days, {} hours, {} minutes, {} seconds".format(*self.equivalent_timer.formatted_time_elapsed))

	def stop_timer_button_callback(self):
		self.equivalent_timer.stop_timer()
		self.update_time_elapsed_label()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)
