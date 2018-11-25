# Module for saving data to json files and loading data from json files.

from json import *
import os.path
import sys

def collect_data_needing_saving(category_manager):
	data_needing_saving = []
	for category in category_manager.category_list:
		list_of_options = []
		for option in category.options_list:
			list_of_responses = []
			for response in option.responses_list:
				response_dict = {'name': response.name, 'times_shown': response.times_shown, 'times_pressed': response.times_pressed}
				list_of_responses.append(response_dict)
			tuple_of_responses = tuple(list_of_responses)
			option_dict = {'name': option.name, 'responses_tuple': tuple_of_responses}
			list_of_options.append(option_dict)
		tuple_of_options = tuple(list_of_options)
		data_in_category_to_save = {'name': category.name, 'options tuple': tuple_of_options}
		data_needing_saving.append(data_in_category_to_save)
	return data_needing_saving

def autosave_data(data_to_dump):
	with open(os.path.join(sys.path[0], 'cravings_app_save_data.json'), "w") as write_file:
		dump(data_to_dump, write_file)

def collect_and_save_data(category_manager):
	data_to_dump = collect_data_needing_saving(category_manager)
	autosave_data(data_to_dump)
