import tkinter as tk
from tkinter import ttk

from ui_components.timer import PomodoroTimer
from ui_components.settings import SettingsTab
import modules.config

if __name__ == "__main__":
	window = tk.Tk()
	window.wm_title("Pomodon't")
	# window.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

	config = modules.config.load_config("config.json")

	n = ttk.Notebook(window)
	timer_tab = ttk.Frame(n)
	config_tab = ttk.Frame(n)
	n.add(timer_tab, text="Timer")
	n.add(config_tab, text="Settings")
	n.pack()

	timer = PomodoroTimer(timer_tab, config)
	timer.grid(0, 0)

	settings = SettingsTab(config_tab, config)
	settings.grid(0, 0)

	window.mainloop()

	modules.config.save_config("config.json", config)
