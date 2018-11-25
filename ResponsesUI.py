from PageUI import *
from tkinter import *
from random import *

class ResponsesUI(PageUI):
	def __init__(self, owning_UI_manager, window, owning_category_UI):
		PageUI.__init__(self, owning_UI_manager, window=window)
		self.response_UIs_to_load = []
		self.done_button = Button(master=window, text='Done',command=self.done_button_callback)
		self.back_button = Button(master=window, text='Back', command=self.back_button_callback)
		self.response_UIs_list = []
		self.owning_category_UI = owning_category_UI

	def recalculate_widgets_in_page(self):
		self.recalculate_response_UIs_to_load()
		self.widgets_in_page = [response_UI.main_button for response_UI in self.response_UIs_to_load]
		self.widgets_in_page += [self.done_button, self.back_button]

	def back_button_callback(self):
		self.owning_UI_manager.go_to_page(self.owning_category_UI.options_ui)

	def done_button_callback(self):
		self.increment_displayed_response_denominators()
		self.increment_selected_response_numerators()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)

	def increment_displayed_response_denominators(self):
		# Wants moving to the Responses.py class.
		pass

	def increment_selected_response_numerators(self):
		# Wants moving to the Responses.py class.
		pass

	def recalculate_response_UIs_to_load(self):
		# First need to work out which options have been pressed.
		# Then need to use some random number generation to decide which ones to load.
		# For now could just make it display all of them. But will need this eventually anyway. 
		response_UIs_to_consider = []
		for option_UI in self.owning_category_UI.options_ui.option_UIs_list:
			if option_UI.corresponding_option.selected == True:
				response_UIs_to_consider += option_UI.response_UIs_list
		relative_probabilities_list = [(response_UI.corresponding_response.times_pressed+1.0)/(response_UI.corresponding_response.times_shown+1.0) for response_UI in response_UIs_to_consider]
		total_probability = sum(relative_probabilities_list)
		absolute_probabilities_list = [relative_probability/ total_probability for relative_probability in relative_probabilities_list]
		cumulative_probabilities_list = [0] * len(absolute_probabilities_list)
		for index in range(len(absolute_probabilities_list)):
			cumulative_probabilities_list[index] = sum(absolute_probabilities_list[:index+1])
		chosen_response_UIs = []
		while (len(chosen_response_UIs) < 5) and (len(chosen_response_UIs) < len(response_UIs_to_consider)):
			random_number = random()
			response_UI_found = False
			current_index = 0
			while not response_UI_found:
				if random_number < cumulative_probabilities_list[current_index]:
					if response_UIs_to_consider[current_index] not in chosen_response_UIs:
						chosen_response_UIs.append(response_UIs_to_consider[current_index])
					response_UI_found = True
				current_index +=1
		self.response_UIs_to_load = chosen_response_UIs

	def load_page(self):
		self.recalculate_widgets_in_page()
		self.reset_responses()
		PageUI.load_page(self)
		for response_UI in self.response_UIs_to_load:
			response_UI.corresponding_response.times_shown+=1

	def reset_responses(self):
		for response_UI in self.response_UIs_to_load:
			response_UI.unpress_button(response_UI.main_button)





