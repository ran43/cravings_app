class UIClass():

	relwidth_button = 0.5
	relwidth_label = 0.9
	anchor = "c"
	relx = 0.5

	def __init__(self, owning_UI_manager):
		self.owning_UI_manager = owning_UI_manager

	def display_button(self, relx = relx, rely, relwidth=relwidth_button, relheight, anchor=anchor, Button):
		"""This function places a button in the main window. If no button is supplied, then the main button belonging to the derived class is used.
		Otherwise, the button supplied is displayed."""
		Button.place(relx=relx, rely=rely, relwidth=rewidth,relheight=relheight,anchor=anchor)

	def display_label(self, relx = relx_label, rely, relwidth=relwidth, relheight, anchor=anchor, Label)
			"""This function places a button in the main window. If no button is supplied, then the main button belonging to the derived class is used.
		Otherwise, the button supplied is displayed."""
		Label.place(relx=relx, rely=rely, relwidth=rewidth,relheight=relheight,anchor=anchor)




		 


