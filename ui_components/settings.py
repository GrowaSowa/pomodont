import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from ui_components.num_input import NumberEntry
from modules.config import AppConfig

class SettingsTab():
	def __init__(self, parent: tk.Misc, config: AppConfig):
		self.parent = parent
		self.config = config

		self.session_entry = TimePicker(parent, config.session_time)
		self.break_entry = TimePicker(parent, config.break_time)

		self.session_label = ttk.Label(parent, text="Session time:")
		self.break_label = ttk.Label(parent, text="Break time:")

		self.save_btn = tk.Button(parent, text="Save")

	def grid(self, root_row: int, root_column: int):
		self.session_label.grid(row=root_row, column=root_column)
		self.session_entry.grid(row=root_row+1, column=root_column)
		self.break_label.grid(row=root_row+2, column=root_column)
		self.break_entry.grid(row=root_row+3, column=root_column)
		self.save_btn.grid(row=root_row+4, column=root_column)

	def save_settings(self):
		self.config.session_time = self.session_entry.get()
		self.config.break_time = self.break_entry.get()

class TimePicker(ttk.Frame):
	def __init__(self, parent: tk.Misc, init_val: tuple[int, int, int], **kwargs):
		super().__init__(parent, **kwargs)

		self.h_entry = NumberEntry(self, init_val[0], 0, 99, 2)
		self.min_entry = NumberEntry(self, init_val[1], 0, 59, 2)
		self.sec_entry = NumberEntry(self, init_val[2], 0, 59, 2)

		self.h_label = ttk.Label(self, text="h", font=tkFont.Font(family="TkTextFont", size=14))
		self.min_label = ttk.Label(self, text="min", font=tkFont.Font(family="TkTextFont", size=14))
		self.sec_label = ttk.Label(self, text="s", font=tkFont.Font(family="TkTextFont", size=14))

		self.h_entry.grid(row=0, column=0)
		self.h_label.grid(row=0, column=1, padx=(0, 10))
		self.min_entry.grid(row=0, column=2)
		self.min_label.grid(row=0, column=3, padx=(0, 10))
		self.sec_entry.grid(row=0, column=4)
		self.sec_label.grid(row=0, column=5)

	def get(self)->tuple[int, int, int]:
		return (self.h_entry.get(), self.min_entry.get(), self.sec_entry.get())
