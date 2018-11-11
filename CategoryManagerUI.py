from PageUI import *
from CategoryUI import *

class CategoryManagerUI(PageUI):
	def __init__(self, owning_UI_manager, equivalent_category_manager):
		self.PageUI.__init(self, owning_UI_manager=owning_UI_manager)
		self.category_UIs_list = []
		self.add_category_button = Button(window=window, text="Add Category", command = self.add_category_button_callback)
		self.delete_category_button = Button(window=window, text="Delete Category")
		self.recalculate_widgets_in_page()
		self.equivalent_category_manager = equivalent_category_manager

	def recalculate_widgets_in_page(self):
		self.widgets_in_page = (self.category_UIs_list.append(add_category_button)).append(delete_category_button)

	def add_category_button_callback(self):
		new_category_name = simpledialog.askstring("Input", "What is the name of the new category?",
                                parent=window)
		new_category = self.equivalent_category_manager.add_category(self, new_category_name=new_category_name)
		self.add_category_UI(self, category=new_category)

	def add_category_UI(self, category):
		self.category_UIs_list.append(CategoryUI(owning_UI_manager=self.owning_UI_manager, category=))