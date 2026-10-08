import tkinter as tk
from tkinter import ttk

from ui_components.num_input import NumberEntry
from modules.config import AppConfig

class SettingsTab():
	def __init__(self, parent: tk.Misc, config: AppConfig):
		self.parent = parent
		self.config = config

	def grid(self, root_row: int, root_column: int):
		pass