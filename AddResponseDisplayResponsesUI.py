from tkinter import *
from PageUI import *

class AddResponseDisplayResponsesUI(PageUI):
	def __init__(self, window, owning_UI_manager, owning_option_UI):
		PageUI.__init__(self, window = window, owning_UI_manager=owning_UI_manager)
		self.owning_option_UI = owning_option_UI
		self.explanatory_label = Label(master=window, text = "These are the existing responses \n to this reason. \n Press the button to add another one.")
		self.back_button = Button(master=window, text = "Back", command=self.back_button_callback)
		self.add_response_button = Button(master=window, text = "Add a Response", command=self.add_response_button_callback)
		self.recalculate_widgets_in_page()


	def recalculate_widgets_in_page(self):
		self.widgets_in_page = [self.explanatory_label] + [response_UI.display_label for response_UI in self.owning_option_UI.response_UIs_list]
		self.widgets_in_page.append(self.add_response_button)
		self.widgets_in_page.append(self.back_button)

	def add_response_button_callback(self):
		new_response_text = simpledialog.askstring("Input", "What would you like the new response to say?",
                        parent=self.window)
		if new_response_text == None:
			return
		new_response_object = self.owning_option_UI.corresponding_option.add_response(text=new_response_text)
		self.owning_option_UI.update_response_UIs_list()
		self.recalculate_widgets_in_page()
		self.owning_UI_manager.go_to_page(self)

	def back_button_callback(self):
		self.owning_UI_manager.go_to_page(self.owning_option_UI.owning_options_UI.owning_category_UI.add_responses_ui)

