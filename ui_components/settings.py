import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from ui_components.num_input import NumberEntry
from modules.config import AppConfig

class SettingsTab(ttk.Frame):
	def __init__(self, parent: tk.Misc, config: AppConfig, **kwargs):
		super().__init__(parent, **kwargs)
		self.config = config

		self.session_entry = TimePicker(self, config.session_time)
		self.break_entry = TimePicker(self, config.break_time)
		self.session_num_entry = NumberEntry(self, self.config.n_sessions, 1, 99, 2)

		self.session_label = ttk.Label(self, text="Session time:")
		self.break_label = ttk.Label(self, text="Break time:")
		self.session_num_label = ttk.Label(self, text="# sessions:")

		self.save_btn = tk.Button(self, text="Save")

		self.session_label.grid(row=0, column=0)
		self.session_entry.grid(row=1, column=0)
		self.break_label.grid(row=2, column=0)
		self.break_entry.grid(row=3, column=0)
		self.session_num_label.grid(row=4, column=0)
		self.session_num_entry.grid(row=5, column=0)
		self.save_btn.grid(row=6, column=0)

	def save_settings(self):
		#TODO: make this actual MVC, rather than direct modification of the model?
		self.config.session_time = self.session_entry.get()
		self.config.break_time = self.break_entry.get()
		self.config.n_sessions = self.session_num_entry.get()

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
