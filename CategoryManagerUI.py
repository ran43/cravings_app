from tkinter import *
from tkinter import simpledialog
from PageUI import *
from CategoryUI import *

class CategoryManagerUI(PageUI):
	def __init__(self, owning_UI_manager, equivalent_category_manager, window):
		PageUI.__init__(self, owning_UI_manager=owning_UI_manager, window=window)
		self.category_UIs_list = list()
		self.add_category_button = Button(master=window, text="Add Category", command = self.add_category_button_callback)
		self.delete_category_button = Button(master=window, text="Delete Category")
		self.equivalent_category_manager = equivalent_category_manager
		self.window = window
		self.owning_UI_manager=owning_UI_manager
		self.recalculate_widgets_in_page()

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = [category_UI.main_button for category_UI in self.category_UIs_list]
		add_and_delete_buttons_list = [self.add_category_button, self.delete_category_button]
		self.widgets_in_page+= add_and_delete_buttons_list

	def add_category_button_callback(self):
		new_category_name = simpledialog.askstring("Input", "What is the name of the new category?",
                                parent=self.window)
		if new_category_name == None:
			return
		new_category = self.equivalent_category_manager.add_category(new_category_name=new_category_name)
		self.add_category_UI(category=new_category)
		self.recalculate_widgets_in_page()
		self.owning_UI_manager.go_to_page(self)

	def add_category_UI(self, category):
		self.category_UIs_list.append(CategoryUI(owning_category_manager_UI=self, owning_UI_manager=self.owning_UI_manager, category=category, window = self.window))