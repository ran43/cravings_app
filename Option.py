# Option
class Option():
	def __init__(self, label, owner):
		self.name = label
		self.responses_list = []
		self.counter = 0
		self.selected = False
		self.owning_category = owner

	def add_response(self):
		pass

	def delete_response(self):
		pass

	def option_button_callback(self):
		if (self.owning_category.total_pressed <5):
			self.select = True
			self.owning_category.total_pressed+=1
			relypos = self.option_button.place_info().get('rely')
			relativeheight = self.option_button.place_info().get('relheight')
			self.option_button.place_forget()
			self.option_button_pressed.place(relx = 0.5, rely = relypos, relwidth = 0.5, anchor = 'c', relheight = relativeheight)
			#self.option_button_pressed.place(relx = 0.5, relwidth = 0.5, rely = rely_pos, relheight = relativeheight, anchor = 'c')
		else:
			pass
			# Print that 5 options have already been chosen.
			# Need to add something to this function to turn the option button blue when it is pressed. I'm wondering about actually making it a separate button as buttons are immutable and therefore reloading the option page every time an option is pressed. Shouldn't actually be much extra work to implement.  

	def unselect_option(self):
		self.selected = False
		self.owning_category.total_pressed-=1