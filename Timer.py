#Timer
class Timer:
	def __init__(self, owning_category):
		self.start_times_list = []
		self.time_elapsed_list = []
		self.time_last_updated_list = []
		self.personal_best = 0
		self.running = False
		self.start_button = Button(window, text = "Start Timer", command = self.start_timer)
		self.end_button = Button(window, text = "Streak Broken", command = self.stop_timer)
		self.update_timer_button = Button(window, text = "Update Timer", command = self.update_timer)
		self.owner = owning_category
		self.time_elapsed_label = Label(window, text = "")
		self.time_elapsed_days = 0
		self.time_elapsed_hours = 0
		self.time_elapsed_minutes = 0
		self.time_elapsed_seconds = 0

	def display_timer(self, relativeypos, relativeheight):
		pass
		self.time_elapsed_label.place(relx = 0.5, rely = relativeypos, relwidth = 0.9, relheight = relativeheight, anchor = 'c')
		# Need to display a label in the top-centre of the category page. Only displayed when the timer is running.

	def display_start_button(self, relativeypos, relativeheight):
		self.start_button.place(relx = 0.5, relwidth = 0.5, anchor = 'c', rely = relativeypos, relheight = relativeheight)

	def display_stop_button(self, relativeypos, relativeheight):
		self.end_button.place(relx = 0.5, relwidth = 0.5, anchor = 'c', rely = relativeypos, relheight = relativeheight)

	def start_timer(self):
		self.start_times_list.append(datetime.now())
		self.time_last_updated_list.append(datetime.now())
		self.time_elapsed_list.append(self.time_last_updated_list[len(self.time_last_updated_list)-1] - self.start_times_list[len(self.start_times_list)-1])
		self.owner.unload_category_page()
		self.running = True
		self.format_time_elapsed()
		self.owner.load_category_page()

	def format_time_elapsed(self):
		most_recent_time_elapsed = self.time_elapsed_list[len(self.time_elapsed_list)-1]
		self.time_elapsed_days = most_recent_time_elapsed.days % 7
		self.time_elapsed_hours = most_recent_time_elapsed.seconds / 3600
		self.time_elapsed_minutes = ((most_recent_time_elapsed.seconds) / 60) % 60
		self.time_elapsed_seconds = most_recent_time_elapsed.seconds % 60
		self.time_elapsed_label = Label(window, text = "{} days, {} hours, {} minutes and {} seconds".format(int(self.time_elapsed_days), int(self.time_elapsed_hours), int(self.time_elapsed_minutes), int(self.time_elapsed_seconds)))

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

	def display_update_timer_button(self, relativeypos, relativeheight):
		self.update_timer_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')