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
		list_of_start_times = []
		for start_time in category.timer.start_times_list:
			list_of_start_times.append({'year': start_time.year, 'month': start_time.month, 'day': start_time.day, 'hour': start_time.hour, 'minute': start_time.minute, 'second': start_time.second})
		list_of_last_updated_times = []
		for last_updated_time in category.timer.time_last_updated_list:
			list_of_last_updated_times.append({'year': last_updated_time.year, 'month': last_updated_time.month, 'day': last_updated_time.day, 'hour': last_updated_time.hour, 'minute': last_updated_time.minute, 'second': last_updated_time.second})
		data_in_category_to_save = {'name': category.name, 'options tuple': tuple_of_options, 'list of start times': list_of_start_times, 'list of last updated times': list_of_last_updated_times}
		data_needing_saving.append(data_in_category_to_save)
	return data_needing_saving

def autosave_data(data_to_dump):
	with open(os.path.join(sys.path[0], 'cravings_app_save_data.json'), "w") as write_file:
		dump(data_to_dump, write_file)

def collect_and_save_data(category_manager):
	data_to_dump = collect_data_needing_saving(category_manager)
	autosave_data(data_to_dump)
