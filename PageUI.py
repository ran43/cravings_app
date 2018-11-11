from UIClass.py import * 

class PageUI(UIClass):
	def __init__(self, owning_UI_manager=owning_UI_manager):
		self.UIClass.__init__(self,owning_UI_manager=owning_UI_manager)
		self.widgets_in_page = []

	def load_page(self):
		number_of_widgets = len(widgets_in_page)
		rely_base_constant = 1.0 / (number_of_widgets + 2)
		relheight_base_expression = 0.75 * rely_base_constant
		for index, widget in enumerate(widgets_in_page):
			assert(widget is (Button || Label))
			if widget is Button:
				widget.display_button(rely=rely_base_constant * (1 + index), relheight = relheight_base_expression, button = widget)
			elif widget is Label:
				widget.display_label(rely=rely_base_constant * (1 + index), relheight = relheight_base_expression, button = widget)
			self.owning_UI_manager.widgts_loaded.append(widget)
