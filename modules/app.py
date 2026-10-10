import tkinter as tk
from tkinter import ttk

from ui_components.timer import PomodoroTimer
from ui_components.settings import SettingsTab
import modules.config

class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.wm_title("Pomodon't")

		self.config = modules.config.load_config("config.json")

		self.tabs = ttk.Notebook(self.window)
		timer_tab = ttk.Frame(self.tabs)
		config_tab = ttk.Frame(self.tabs)
		self.tabs.add(timer_tab, text="Timer")
		self.tabs.add(config_tab, text="Settings")
		self.tabs.pack()
	
		self.timer = PomodoroTimer(timer_tab, self.config)
		self.timer.grid(0, 0)
	
		self.settings = SettingsTab(config_tab, self.config)
		self.settings.save_btn.bind("<Button>", self.save_settings)
		self.settings.grid(0, 0)

	def mainloop(self):
		self.window.mainloop()

	def save_settings(self, event):
		self.settings.save_settings()
		self.timer.reset_timer()