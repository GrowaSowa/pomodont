import tkinter as tk
from tkinter import ttk

from ui_components.timer import PomodoroTimer

if __name__ == "__main__":
	window = tk.Tk()
	window.wm_title("Pomodon't")
	# window.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

	timer = PomodoroTimer(window)
	timer.grid(0, 0)

	window.mainloop()