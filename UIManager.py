from tkinter import *

class UIManager.py(UIClass):
	""" The UIManager handles all of the loading and unloading of pages. It also owns a list of CategoryUIs. """
	def __init__(self):
		self.widgets_loaded = []
		self.category_UIs_list = []

	def go_to_page(self, page):
		""" This will unload the currently loaded page and load the page 'page'
		pass"""

	def unload_page(self):
		"""Unplaces all currently placed widgets, as stored in widgets_loaded"""

	
