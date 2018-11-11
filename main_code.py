from CategoryManager import *
from UIManager import *
from CategoryManagerUI import *

# Set-up
window = Tk()
 
window.title("Crest the Wave")

window.geometry('350x500')
UI_manager = UIManager()
category_manager = CategoryManager()
category_manager_UI = CategoryManagerUI(owning_UI_manager=UI_manager, equivalent_category_manager=category_manager, window=window)
UI_manager.go_to_page(page=category_manager_UI)


window.mainloop()








# #Initialising the Category List
# category_list = CategoryList()
# #Adding categories.
# category_list.category_list.append(Category("Chocolate", window, category_list))
# category_list.category_list.append(Category("Caffeine", window, category_list))
# category_list.category_list.append(Category("Overspending", window, category_list))

# # Adding options to the Chocolate category.
# category_list.category_list[0].options_list.append(Option("Tired", category_list.category_list[0]))
# category_list.category_list[0].options_list.append(Option("Hungry", category_list.category_list[0]))
# category_list.category_list[0].options_list.append(Option("Habit", category_list.category_list[0]))
# category_list.category_list[0].options_list.append(Option("Special Occasion", category_list.category_list[0]))
# category_list.category_list[0].options_list.append(Option("Desire to Treat Myself", category_list.category_list[0]))

# # Loading the categories page:
# category_list.load_categories_page()

