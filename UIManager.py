class UIManager:
	""" Currently a dumping ground for all of the UI related functions. Need to sort this out later and work out what I actually need."""

	def __init__(self):
		self.category_button = Button(window, text = label, command = self.pressed_callback)
		# This counter keeps track of how many options are currently pressed. There is a maximum of 5, which is checked at the start of the callback for pressing an option button. 
		self.next_button = Button(window, text = 'NEXT', command = self.next_callback)
		# This is displayed below the timer 'update timer' button in the category page. Pressing it will increment the cravings counter by 1 and will load the options page.  
		self.craving_button = Button(window, text = 'Craving', command = self.craving_button_callback)
		# This button will be displayed below the responses in the responses page. Pressing it will increment the response counters and will load the category page. 
		self.done_button = Button(window, text = 'Done')
		# This attribute represents whether the button is currently pressed. Not sure it's really needed tbh.
		self.history_button = Button(window, text = "History", command = self.load_history_page)
		# This button is visible at the top-right? of the category page and pressing it will call the load_stats_page() function. 
		self.stats_button = Button(window, text = "Statistics", command = self.load_stats_page())
		# This button is used to go back to the previous page. With the way that it currently works you can only go back from the category page to the main page. 
		self.back_button = Button(window, text = "BACK", command = self.back_button_callback)
		self.achievements_button = Button(window, text = "Achievements", command = self.achievements_button_callback)
		# This is the CategoryList object that owns the category. Only expecting one of these in the program but need to be able to do callbacks to it eg. to unload the front page. And to go back to it. 
		self.option_button = Button(window, text = label, command = self.option_button_callback)
		self.option_button_pressed = Button(window, text = label, highlightbackground="blue", fg = "blue", command = self.unpress_option_button)


	def display_categories(self):
		for index, category in enumerate(self.category_list):
			category.display_category_button((index+1.0)/(4+len(self.category_list)), (3.0/4.0)/(len(self.category_list)+4.0))
	
	def undisplay_categories(self):
	for category in self.category_list:
		category.category_button.place_forget()

	def load_categories_page(self):
		self.display_categories()
		self.display_add_category_button()
		self.display_delete_category_button()	

	def display_add_category_button(self):
		pass

	def display_delete_category_button(self):
		pass	

	def display_category_button(self, relativeypos, relativeheight):
		self.category_button.place(relx = 0.5, rely = relativeypos, relwidth = 0.5, relheight = relativeheight, anchor = 'c')

	def load_category_page(self):
		# Things to potentially display from top to bottom:
		# 1. Timer
		# 2. Start timer
		# 3. Update timer
		# 4. Craving
		# 5. Streak broken
		# 6. Statistics
		# 7. History
		# 8. Achievements
		# 9. Back
		self.category_page_loaded = True
		if (not self.timer.running):
			total_buttons_etc = 4
			relative_y_pos_expression = 1.0/ (total_buttons_etc + 1.0)
			relative_height_expression = (3.0/4.0) / (total_buttons_etc + 1.0)
			self.timer.display_start_button(relativeypos = 1.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_stats_button(relativeypos = 2.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_history_button(relativeypos = 3.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_back_button(relativeypos = 4.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
		else:
			total_buttons_etc = 8
			relative_y_pos_expression = 1.0/ (total_buttons_etc + 1.0)
			relative_height_expression = (3.0/4.0) / (total_buttons_etc + 1.0)
			self.timer.display_timer(relativeypos = relative_y_pos_expression, relativeheight = relative_height_expression)
			self.timer.display_update_timer_button(relativeypos = 2.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_craving_button(relativeypos = 3.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.timer.display_stop_button(relativeypos = 4.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_stats_button(relativeypos = 5.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_history_button(relativeypos = 6.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_achievements_button(relativeypos = 7.0 * relative_y_pos_expression, relativeheight = relative_height_expression)
			self.display_back_button(relativeypos = 8.0 * relative_y_pos_expression, relativeheight = relative_height_expression)

	def unload_category_page(self):
		self.category_page_loaded = False
		if not self.timer.running:
			self.timer.start_button.place_forget()
			self.stats_button.place_forget()
			self.history_button.place_forget()
			self.back_button.place_forget()
		else:
			self.timer.time_elapsed_label.place_forget()
			self.timer.update_timer_button.place_forget()
			self.craving_button.place_forget()
			self.timer.end_button.place_forget()
			self.stats_button.place_forget()
			self.history_button.place_forget()
			self.achievements_button.place_forget()
			self.back_button.place_forget()

	def display_options(self):
		for index, option in enumerate(self.options_list):
			option.option_button.place(relx=.5, rely=index/len(options_list), relheight = 0.75/index, relwidth = 0.5, anchor="c")

	def display_history_button(self, relativeypos, relativeheight):
		self.history_button.place(relx = 0.5, rely = relativeypos, relwidth = 0.5, relheight = relativeheight, anchor = 'c')
		# This is just called when you're on the category page. Could be in the top-left. Then if the button is pressed then want to undisplay all the rest of it and bring up the history page --> need a load_history_page function.

	def load_history_page(self):
		pass
		# This will be the callback function for if the history button is pressed. Displays the history data from the Timer data member of the category. Also need a back button. 

	def display_stats_button(self, relativeypos, relativeheight):
		self.stats_button.place(relx = 0.5, rely = relativeypos, relwidth = 0.5, relheight = relativeheight, anchor = 'c')
		# This will be called on the category page. The button will be in the top-right. Pressing it will call the load_stats_page function.

	def load_stats_page(self):
		pass

		def load_options_page(self):
		self.options_page_loaded = True
		number_of_buttons = len(self.options_list) + 2.0
		relative_y_pos_expression = relative_y_pos_expression = 1.0/ (number_of_buttons + 1.0)
		relative_height_expression = (3.0/4.0) / (number_of_buttons + 1.0)
		for index, option in enumerate(self.options_list):
			option.display_option_button(relativeypos = (index + 1.0) * relative_y_pos_expression, relativeheight = relative_height_expression)
		self.display_next_button(relativeypos = (len(self.options_list)+1.0) * relative_y_pos_expression, relativeheight = relative_height_expression)
		self.display_back_button(relativeypos = (len(self.options_list)+2.0)*relative_y_pos_expression, relativeheight = relative_height_expression)

	def unload_options_page(self):
		self.total_pressed = 0
		self.options_page_loaded = False
		for option in self.options_list:
			if option.pressed:
				option.option_button_pressed.place_forget()
				print(option.name)
				print("Reached option button pressed place forget")
			else:
				option.option_button.place_forget()
				print(option.name)
				print("Reached option button not pressed place forget")
		self.next_button.place_forget()
		self.back_button.place_forget()
		self.unset_option_selections()

	def display_next_button(self, relativeypos, relativeheight):
		self.next_button.place(relx = 0.5, rely = relativeypos, relwidth = 0.5, relheight = relativeheight, anchor = 'c')

	def load_responses_page(self):
		pass

	def display_achievements_button(self, relativeypos, relativeheight):
		self.achievements_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def display_back_button(self, relativeypos, relativeheight):
		self.back_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def display_craving_button(self, relativeypos, relativeheight):
		self.craving_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def display_timer(self, relativeypos, relativeheight):
		self.time_elapsed_label.place(relx = 0.5, rely = relativeypos, relwidth = 0.9, relheight = relativeheight, anchor = 'c')
		# Need to display a label in the top-centre of the category page. Only displayed when the timer is running.

	def display_start_button(self, relativeypos, relativeheight):
		self.start_button.place(relx = 0.5, relwidth = 0.5, anchor = 'c', rely = relativeypos, relheight = relativeheight)

	def display_stop_button(self, relativeypos, relativeheight):
		self.end_button.place(relx = 0.5, relwidth = 0.5, anchor = 'c', rely = relativeypos, relheight = relativeheight)

	def display_update_timer_button(self, relativeypos, relativeheight):
		self.update_timer_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def display_option_button(self, relativeypos, relativeheight):
		self.option_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')



