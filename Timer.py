from datetime import *
from math import *

class Timer:
	def __init__(self, owning_category):
		self.start_times_list = []
		self.time_elapsed_list = []
		self.time_last_updated_list = []
		self.personal_best = 0
		self.running = False
		self.owner = owning_category
		self.time_elapsed_days = 0
		self.time_elapsed_hours = 0
		self.time_elapsed_minutes = 0
		self.time_elapsed_seconds = 0
		self.formatted_time_elapsed = [0] * 4

	def start_timer(self):
		self.start_times_list.append(datetime.now())
		self.time_last_updated_list.append(datetime.now())
		self.time_elapsed_list.append(self.time_last_updated_list[-1] - self.start_times_list[-1])
		self.running = True
		self.format_time_elapsed()

	def format_time_elapsed(self):
		most_recent_time_elapsed = self.time_elapsed_list[-1]
		self.time_elapsed_days = floor(most_recent_time_elapsed.days % 7)
		self.time_elapsed_hours = floor(most_recent_time_elapsed.seconds / 3600)
		self.time_elapsed_minutes = floor(((most_recent_time_elapsed.seconds) / 60) % 60)
		self.time_elapsed_seconds = floor(most_recent_time_elapsed.seconds % 60)
		self.formatted_time_elapsed = [self.time_elapsed_days, self.time_elapsed_hours, self.time_elapsed_minutes, self.time_elapsed_seconds]

	def stop_timer(self):
		self.running = False

	def update_timer(self):
		# Takes the current time, subtracts from it the most recent start time (given by the entry at the end of the start_times_list and stores the result in self.time_elapsed. This is called when the update button is pressed. )
		self.time_last_updated_list[-1] = datetime.now()
		self.time_elapsed_list[-1] = self.time_last_updated_list[-1] - self.start_times_list[-1]
		self.format_time_elapsed()
