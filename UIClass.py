class UIClass():

    relwidth_button = 0.5
    relwidth_label = 0.9
    anchor = "c"
    relx = 0.5

    def __init__(self, owning_UI_manager, window):
        self.owning_UI_manager = owning_UI_manager
        self.window=window

    def display_button(self, button, rely, relheight, relx=0, relwidth=0, anchor=0):
        """This function places a button in the main window. If no button is supplied, then the main button belonging to the derived class is used.
        Otherwise, the button supplied is displayed."""
        if relx == 0:
        	relx = UIClass.relx

        if relwidth == 0:
        	relwidth = UIClass.relwidth_button

        if anchor == 0:
        	anchor = UIClass.anchor
        button.place(relx=relx, rely=rely, relwidth=relwidth,relheight=relheight,anchor=anchor)

    def display_label(self, rely, relheight, label, relx = 0, relwidth=0, anchor=0):
        if relx == 0:
            relx = UIClass.relx

        if relwidth== 0:
            relwidth = UIClass.relwidth_label

        if anchor == 0:
            anchor = UIClass.anchor
        label.place(relx=relx, rely=rely, relwidth=relwidth,relheight=relheight,anchor=anchor)




		 


