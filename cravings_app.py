"""Cravings App"""

from tkinter import *
from datetime import *

#Class Definitions

# Category
class CategoryList():
	def __init__(self):
		self.category_list = []

	def undisplay_categories(self):
		for category in self.category_list:
			category.category_button.place_forget()

	def load_categories_page(self):
		self.display_categories()
		self.display_add_category_button()
		self.display_delete_category_button()

	def display_categories(self):
		for index, category in enumerate(self.category_list):
			category.display_category_button((index+1.0)/(4+len(self.category_list)), (3.0/4.0)/(len(self.category_list)+4.0))
			

	def display_add_category_button(self):
		pass

	def display_delete_category_button(self):
		pass

class Category():
	def __init__(self, label, window, category_list):
		"""Initialises an object of the Category class. This object owns all of the data about that category."""
		# This is the name of the category that will be displayed on the button for the category. Should maybe also be at the top of the category page? Above the timer. 
		self.name = label
		# This keeps track of the current time elapsed and the ones for previous streaks. 
		self.timer = Timer(self)
		# This is a list of Option objects that belong to this category.
		self.options_list = []
		# This is the Achievements object that belongs to the category. It contains lists of Achievement objects, which each have a name, winning condition and a boolean for whether it has been achieved or not. 
		self.achievements = Achievements()
		# Next button. This is displayed below the options in the options screen. 
		self.next_button = Button(window, text = 'NEXT', command = self.next_callback)
		# This is displayed below the timer 'update timer' button in the category page. Pressing it will increment the cravings counter by 1 and will load the options page.  
		self.craving_button = Button(window, text = 'Craving', command = self.craving_button_callback)
		# This button will be displayed below the responses in the responses page. Pressing it will increment the response counters and will load the category page. 
		self.done_button = Button(window, text = 'Done')
		# This attribute represents whether the button is currently pressed. Not sure it's really needed tbh.
		self.pressed = False
		# This button is visible in the main page. Pressing it will take the user to the category page. 
		self.category_button = Button(window, text = label, command = self.pressed_callback)
		# This counter keeps track of how many options are currently pressed. There is a maximum of 5, which is checked at the start of the callback for pressing an option button. 
		self.total_pressed = 0
		# This button is visible at the top-left? of the category page and pressing it will call the load_history_page() function. 
		self.history_button = Button(window, text = "History", command = self.load_history_page)
		# This button is visible at the top-right? of the category page and pressing it will call the load_stats_page() function. 
		self.stats_button = Button(window, text = "Statistics", command = self.load_stats_page())
		# This button is used to go back to the previous page. With the way that it currently works you can only go back from the category page to the main page. 
		self.back_button = Button(window, text = "BACK", command = self.back_button_callback)
		self.achievements_button = Button(window, text = "Achievements", command = self.achievements_button_callback)
		# This is the CategoryList object that owns the category. Only expecting one of these in the program but need to be able to do callbacks to it eg. to unload the front page. And to go back to it. 
		self.owner = category_list
		# This keeps track of the total number of times that the cravings button has been pressed. This information is available in the stats page and is used to award achievements. 
		self.cravings_counter = 0
		self.category_page_loaded = False
		self.options_page_loaded = False

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

		#self.display_history_button()
		#self.display_stats_button()

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

	def add_option(self):
		# This is a callback function from the add_option button.
		# The user can input the name of this option, which is then appended to the options_list.
		# Need a way of adding responses to the new option. Need to decide how to do this.
		pass

	def delete_option(self):
		# Callback function from the delete_option button. How exactly will this work? Will there be one delete_option button and then that takes you to another page in which you can delete options? Or will it be an option from each of the options within the option list. 
		# Needs to check that you really want to delete the option.
		# Also, it would be good if you could manage the options without having to press the craving button - could there be a manage options option within the main page for the category as well? Also want to add and delete them on the fly after pressing Craving I think. 
		pass

	def increment_selected_options(self):
		for option in self.options_list:
			if option.pressed:
				option.counter+=1
		# This is one of the functions that should be called upon pressing the 'Next' button as you're then going on to the responses screen and need to increment the options before you do that. 

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

	def pressed_callback(self):
		self.pressed = True
		self.owner.undisplay_categories() # Need to define this.
		self.load_category_page()

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

	def return_to_main_page(self):
		self.unload_category_page()
		self.owner.load_categories_page()

	def display_back_button(self, relativeypos, relativeheight):
		self.back_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def display_craving_button(self, relativeypos, relativeheight):
		self.craving_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def craving_button_callback(self):
		self.unload_category_page()
		self.cravings_counter+=1
		self.load_options_page()

	def display_achievements_button(self, relativeypos, relativeheight):
		self.achievements_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def achievements_button_callback(self):
		self.unload_category_page()
		self.achievements.load_achievements_page() #### The interpreter is claiming that this is taking an argument but it clearly isn't. What's going on? 

	def back_button_callback(self):
		if self.category_page_loaded:
			self.return_to_main_page()
		elif self.options_page_loaded:
			self.return_to_category_page()

	def return_to_category_page(self):
		self.unload_options_page()
		self.load_category_page()

	def next_callback(self):
		self.increment_selected_options()
		self.unload_options_page()
		#self.load_responses_page()

	def unset_option_selections(self):
		for option in self.options_list:
			option.pressed = False


# Option
class Option():
	def __init__(self, label, owner):
		self.name = label
		self.responses_list = []
		self.counter = 0
		self.pressed = False
		self.owning_category = owner
		self.option_button = Button(window, text = label, command = self.option_button_callback)
		self.option_button_pressed = Button(window, text = label, highlightbackground="blue", fg = "blue", command = self.unpress_option_button)

	def add_response(self):
		pass

	def delete_response(self):
		pass

	def option_button_callback(self):
		if (self.owning_category.total_pressed <5):
			self.pressed = True
			self.owning_category.total_pressed+=1
			relypos = self.option_button.place_info().get('rely')
			relativeheight = self.option_button.place_info().get('relheight')
			self.option_button.place_forget()
			self.option_button_pressed.place(relx = 0.5, rely = relypos, relwidth = 0.5, anchor = 'c', relheight = relativeheight)
			#self.option_button_pressed.place(relx = 0.5, relwidth = 0.5, rely = rely_pos, relheight = relativeheight, anchor = 'c')
		else:
			pass
			# Print that 5 options have already been chosen.
			# Need to add something to this function to turn the option button blue when it is pressed. I'm wondering about actually making it a separate button as buttons are immutable and therefore reloading the option page every time an option is pressed. Shouldn't actually be much extra work to implement.  

	def display_option_button(self, relativeypos, relativeheight):
		self.option_button.place(relx = 0.5, relwidth = 0.5, rely = relativeypos, relheight = relativeheight, anchor = 'c')

	def unpress_option_button(self):
		self.pressed = False
		self.owning_category.total_pressed-=1
		relypos = self.option_button_pressed.place_info().get('rely')
		relativeheight = self.option_button_pressed.place_info().get('relheight')
		self.option_button_pressed.place_forget()
		self.display_option_button(relativeypos = relypos, relativeheight = relativeheight)

#Achievements
class Achievements:
	def __init__(self):
		time_achievements_list = []
		cravings_beaten_achievements_list = []
		personal_best_achievement = Achievement()

	def load_achievements_page(self):
		pass
		# This should display the achievements in some way that I'm not quite clear on quite yet. Grey-out the ones that haven't been won yet. 

#Achievement
class Achievement:
	def __init__(self):
		self.achieved = False
		self.name = ""

class TimeAchievement(Achievement):
	def __init__(self, time_needed):
		self.Achievement.__init__()
		self.time_required = time_needed

class CravingsAchievement(Achievement):
	def __init__(self, cravings_needing_beating):
		self.Achievement.__init__()
		self.cravings_to_beat = cravings_needing_beating

#Response
class Response():
	def __init__(self, label):
		self.name = label
		self.counter = 0

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

# Initialising the Window.
window = Tk()
 
window.title("Crest the Wave")

window.geometry('350x500')


#Initialising the Category List
category_list = CategoryList()
#Adding categories.
category_list.category_list.append(Category("Chocolate", window, category_list))
category_list.category_list.append(Category("Caffeine", window, category_list))
category_list.category_list.append(Category("Overspending", window, category_list))

# Adding options to the Chocolate category.
category_list.category_list[0].options_list.append(Option("Tired", category_list.category_list[0]))
category_list.category_list[0].options_list.append(Option("Hungry", category_list.category_list[0]))
category_list.category_list[0].options_list.append(Option("Habit", category_list.category_list[0]))
category_list.category_list[0].options_list.append(Option("Special Occasion", category_list.category_list[0]))
category_list.category_list[0].options_list.append(Option("Desire to Treat Myself", category_list.category_list[0]))

# Loading the categories page:
category_list.load_categories_page()


window.mainloop()