from datetime import *

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
		self.time_elapsed_list.append(self.time_last_updated_list[len(self.time_last_updated_list)-1] - self.start_times_list[len(self.start_times_list)-1])
		self.running = True
		self.format_time_elapsed()

	def format_time_elapsed(self):
		most_recent_time_elapsed = self.time_elapsed_list[-1]
		self.time_elapsed_days = most_recent_time_elapsed.days % 7
		self.time_elapsed_hours = most_recent_time_elapsed.seconds / 3600
		self.time_elapsed_minutes = ((most_recent_time_elapsed.seconds) / 60) % 60
		self.time_elapsed_seconds = most_recent_time_elapsed.seconds % 60
		self.formatted_time_elapsed = [self.time_elapsed_days, self.time_elapsed_hours, self.time_elapsed_minutes, self.time_elapsed_seconds]

	def stop_timer(self):
		self.owner.unload_category_page()
		self.running = False
		self.owner.load_category_page()

	def update_timer(self):
		# Takes the current time, subtracts from it the most recent start time (given by the entry at the end of the start_times_list and stores the result in self.time_elapsed. This is called when the update button is pressed. )
		current_index = len(self.time_last_updated_list) - 1
		self.time_last_updated_list[current_index] = datetime.now()
		self.time_elapsed_list[current_index] = self.time_last_updated_list[current_index] - self.start_times_list[current_index]
		self.owner.unload_category_page()
		self.format_time_elapsed()
		self.owner.load_category_page()
