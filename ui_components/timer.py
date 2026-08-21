import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from pygame import mixer

SESSION_TIME = (0, 25, 0)
BREAK_TIME = (0, 5, 0)
N_SESSIONS = 4

SESSION_BAR_COLOR = "blue"
BREAK_BAR_COLOR = "green"
PAUSE_BAR_COLOR = "grey"

SESSION_END_SOUND = "D:\\backup_new\\music\\effects\\aughhh.mp3"
BREAK_END_SOUND = "D:\\backup_new\\music\\effects\\quack.mp3"

class Time():
	def __init__(self, start_t: tuple[int, int, int]):
		hours, minutes, seconds = start_t
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		# self.miliseconds = 0

	def decrement(self):
		if self.seconds == 0:
			if self.minutes == 0:
				if self.hours == 0:
					return False
				else:
					self.hours -= 1
					self.minutes = 59
					self.seconds = 59
			else:
				self.minutes -= 1
				self.seconds += 59
		else:
			self.seconds -= 1
		return True

	def get_seconds(self):
		return self.hours * 3600 + self.minutes * 60 + self.seconds

class PomodoroTimer():
	def __init__(self, parent: tk.Misc):
		self.parent = parent
		self.session_time = SESSION_TIME
		self.break_time = BREAK_TIME
		self.n_sessions: int = N_SESSIONS
		self.current_time = Time((0, 0, 0))
		self.session_n = 0
		self.is_running = False
		self.is_break = False
		self.is_paused = False

		self.ses_disp_str = tk.StringVar(value="Session 0/0:")
		self.tmr_disp_str = tk.StringVar(value="00:00:00")
		self.session_display = ttk.Label(parent, textvariable=self.ses_disp_str, font=tkFont.Font(family="Consolas", size=30))
		self.timer_display = ttk.Label(parent, textvariable=self.tmr_disp_str, font=tkFont.Font(family="Consolas", size=45))

		self.start_btn = tk.Button(parent, text="Start", command=self.initialize_timer)
		self.pause_btn = tk.Button(parent, text="Pause/Unpause", command=self.pause_unpause_timer)
		self.reset_btn = tk.Button(parent, text="Reset", command=self.reset_timer)

		self.prog_bar = TimerProgressBar(parent)

		mixer.init()
		self.ses_end_snd = mixer.Sound(SESSION_END_SOUND)
		self.brk_end_snd = mixer.Sound(BREAK_END_SOUND)

	def grid(self, root_row: int, root_column: int):
		self.session_display.grid(row=root_row, column=root_column, columnspan=3)
		self.timer_display.grid(row=root_row+1, column=root_column, columnspan=3)
		self.prog_bar.grid(root_row+2, root_column)
		self.start_btn.grid(row=root_row+3, column=root_column)
		self.pause_btn.grid(row=root_row+3, column=root_column+1)
		self.reset_btn.grid(row=root_row+3, column=root_column+2)

	def initialize_timer(self):
		self.is_break = False
		self.session_n = 1
		self.start_timer()

	def start_timer(self):
		self.is_running = True
		self.is_paused = False
		self.current_time = Time(self.break_time) if self.is_break else Time(self.session_time)
		self.update_timer()

	def update_timer(self):
		if not self.is_running:
			return
		if self.is_paused:
			self.parent.after(ms=100, func=self.update_timer)
			return

		is_ongoing = self.current_time.decrement()
		self.update_bar()

		if self.is_break:
			self.ses_disp_str.set(f"Break {self.session_n}/{self.n_sessions}:")
		else:
			self.ses_disp_str.set(f"Session {self.session_n}/{self.n_sessions}:")
		self.tmr_disp_str.set(f"{self.current_time.hours:02d}:{self.current_time.minutes:02d}:{self.current_time.seconds:02d}")

		if is_ongoing:
			self.parent.after(ms=1000, func=self.update_timer)
		else:
			self.progress_session()

	def update_bar(self):
		self.prog_bar.update(self.current_time.get_seconds(), self.is_running, self.is_paused, self.is_break)

	def progress_session(self):
		if self.session_n == self.n_sessions:
			self.ses_end_snd.play()
			self.is_running = False
			self.update_bar()
			messagebox.showinfo("Time Countdown", "Time's up ")
			return
		if self.is_break:
			self.session_n += 1
			self.brk_end_snd.play()
		else:
			self.ses_end_snd.play()
		self.is_break = not self.is_break
		self.parent.after(ms=100, func=self.start_timer)

	def pause_unpause_timer(self):
		self.is_paused = not self.is_paused
		self.update_bar()

	def reset_timer(self):
		self.is_running = False
		self.ses_disp_str.set(f"Session 0/0:")
		self.tmr_disp_str.set(f"00:00:00")
		self.update_bar()

class TimerProgressBar():
	def __init__(self, parent: tk.Misc) -> None:
		self.parent = parent
		self.bar = tk.Canvas(parent, width=200, height=10)

	def grid(self, root_row: int, root_column: int):
		self.bar.grid(row=root_row, column=root_column, columnspan=3)
		self.bar.create_rectangle(0, 0, 200, 10, fill="black", outline="black")

	def update(self, current_t: int, is_running: bool, is_paused: bool, is_break: bool):
		def get_bar_color():
			if is_paused:
				return PAUSE_BAR_COLOR
			if is_break:
				return BREAK_BAR_COLOR
			return SESSION_BAR_COLOR

		self.bar.create_rectangle(0, 0, 200, 10, fill="black", outline="black")
		if is_running:
			bar_color = get_bar_color()
			full_t = Time(BREAK_TIME).get_seconds() if is_break else Time(SESSION_TIME).get_seconds()
			width = int(200 * (1 - current_t/full_t))
			self.bar.create_rectangle(0, 0, width, 10, fill=bar_color, outline=bar_color)

	