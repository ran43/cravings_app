from Timer import *
from Achievements import *
from Option import *

class Category():
	def __init__(self, label, category_manager):
		"""Initialises an object of the Category class. This object owns all of the data about that category."""
		# This is the name of the category that will be displayed on the button for the category. Should maybe also be at the top of the category page? Above the timer. 
		self.name = label
		# This keeps track of the current time elapsed and the ones for previous streaks. 
		self.timer = Timer(self)
		# This is a list of Option objects that belong to this category.
		self.options_list = []
		# This is the Achievements object that belongs to the category. It contains lists of Achievement objects, which each have a name, winning condition and a boolean for whether it has been achieved or not. 
		self.achievements = Achievements()
		self.in_category = False
		# This button is visible in the main page. Pressing it will take the user to the category page. 
		self.total_pressed = 0
		# This button is visible at the top-left? of the category page and pressing it will call the load_history_page() function. 
		self.owner = category_manager
		# This keeps track of the total number of times that the cravings button has been pressed. This information is available in the stats page and is used to award achievements. 
		self.cravings_counter = 0

		#self.display_history_button()
		#self.display_stats_button()

	def add_option(self,label):
		new_option = Option(label=label, owner=self)
		self.options_list.append(new_option)
		return new_option

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

	def unset_option_selections(self):
		for option in self.options_list:
			option.pressed = False

	def increment_cravings_counter(self):
		self.cravings_counter+=1

	def decrement_cravings_counter(self):
		self.cravings_counter-=1

# """ All to be moved?"""
# 	def pressed_callback(self):
# 		self.pressed = True
# 		self.owner.undisplay_categories() # Need to define this.
# 		self.load_category_page()

# 	def craving_button_callback(self):
# 		self.unload_category_page()
# 		self.cravings_counter+=1
# 		self.load_options_page()

# 	def achievements_button_callback(self):
# 		self.unload_category_page()
# 		self.achievements.load_achievements_page() #### The interpreter is claiming that this is taking an argument but it clearly isn't. What's going on? 

# 	def back_button_callback(self):
# 		if self.category_page_loaded:
# 			self.return_to_main_page()
# 		elif self.options_page_loaded:
# 			self.return_to_category_page()

# 	def return_to_category_page(self):
# 		self.unload_options_page()
# 		self.load_category_page()

# 	def next_callback(self):
# 		self.increment_selected_options()
# 		self.unload_options_page()
# 		#self.load_responses_page()

# 	def return_to_main_page(self):
# 		self.unload_category_page()
# 		self.owner.load_categories_page()

# 	def load_achievements_page(self):
# 		pass
# 		# This should display the achievements in some way that I'm not quite clear on quite yet. Grey-out the ones that haven't been won yet. 

