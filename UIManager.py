from tkinter import *
from UIClass import *

class UIManager(UIClass):
	""" The UIManager handles all of the loading and unloading of pages. It also owns a list of CategoryUIs. """
	def __init__(self):
		self.widgets_loaded = []
		self.category_UIs_list = []

	def go_to_page(self, page):
		""" This will unload the currently loaded page and load the page 'page'"""
		self.unload_page()
		page.load_page()

	def unload_page(self):
		"""Unplaces all currently placed widgets, as stored in widgets_loaded"""
		for widget in self.widgets_loaded:
			widget.place_forget()
		self.widgets_loaded = []



