from PageUI import *
from CategoryUI import *
from Category import *
from OptionUI import *
from ResponsesUI import *

class OptionsUI(PageUI):
	def __init__(self, owning_category_UI, owning_UI_manager, window):
		PageUI.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.option_UIs_list = []
		self.owning_category_UI = owning_category_UI
		self.main_button = Button(master=window, text="Craving", command=self.craving_button_callback) # Need to add a callback to this. 
		self.window = window
		self.explanatory_label = Label(master=self.window, text=" Please select the options that apply\n\n at present (up to 5) and press 'Next'.")
		self.add_option_button = Button(master=self.window, text="Add Reason", command=self.add_option_button_callback)
		self.next_button = Button(master=self.window, text="Next", command=self.next_button_callback)
		self.back_button = Button(master=self.window, text = "Back", command=self.back_button_callback)
		self.recalculate_widgets_in_page()
		self.responses_ui = ResponsesUI(window=window, owning_UI_manager=owning_UI_manager)

	def craving_button_callback(self):
		self.owning_category_UI.category_represented.increment_cravings_counter()
		self.owning_UI_manager.go_to_page(self)

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = [self.explanatory_label] + [option_UI.main_button for option_UI in self.option_UIs_list]
		self.widgets_in_page.append(self.add_option_button)
		self.widgets_in_page.append(self.next_button)
		self.widgets_in_page.append(self.back_button)

	def add_option_button_callback(self):
		new_option_name = simpledialog.askstring("Input", "What is the the new reason?",
                                parent=self.window)
		if new_option_name == None:
			return
		new_option = self.owning_category_UI.category_represented.add_option(label=new_option_name)
		self.add_option_UI(option=new_option, label=new_option_name, new_option=new_option)
		self.recalculate_widgets_in_page()
		self.owning_UI_manager.go_to_page(self)

	def add_option_UI(self, option, label, new_option):
		new_option_UI = OptionUI(owning_UI_manager=self.owning_UI_manager, window=self.window, label=label, option=new_option, owning_options_UI=self)
		self.option_UIs_list.append(new_option_UI)

	def back_button_callback(self):
		self.owning_category_UI.category_represented.decrement_cravings_counter()
		self.reset_options_selected()
		self.owning_UI_manager.go_to_page(self.owning_category_UI)

	def reset_options_selected(self):
		for option_UI in self.option_UIs_list:
			option_UI.unpress_button(option_UI.main_button)

	def next_button_callback(self):
		self.owning_UI_manager.go_to_page(self.responses_ui)
		self.reset_options_selected()




		