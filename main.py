import tkinter as tk
from tkinter import ttk

from ui_components.timer import PomodoroTimer
import modules.config

if __name__ == "__main__":
	window = tk.Tk()
	window.wm_title("Pomodon't")
	# window.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

	config = modules.config.load_config("config.json")

	timer = PomodoroTimer(window, config)
	timer.grid(0, 0)

	window.mainloop()

	modules.config.save_config("config.json", config)
