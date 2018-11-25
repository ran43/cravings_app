from CategoryManager import *
from UIManager import *
from CategoryManagerUI import *
from LoadSaveData import *

# Set-up
window = Tk()
 
window.title("Crest the Wave")

window.geometry('350x500')
UI_manager = UIManager()
category_manager = CategoryManager()
collect_and_save_data(category_manager)

category_manager_UI = CategoryManagerUI(owning_UI_manager=UI_manager, equivalent_category_manager=category_manager, window=window)
UI_manager.go_to_page(page=category_manager_UI)


window.mainloop()
