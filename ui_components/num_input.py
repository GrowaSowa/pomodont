import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class NumberEntry(ttk.Frame):
	def __init__(self, parent: tk.Misc, value: int = 0, min_val: int|None = None, max_val: int|None = None, width: int = 8, **kwargs):
		super().__init__(parent, **kwargs)
		self.min_val = min_val
		self.max_val = max_val

		self.val = tk.StringVar(value=str(value))
		self.entry = ttk.Entry(self, textvariable=self.val, width=width, justify="right", font=tkFont.Font(family="TkTextFont", size=14), validate="key", validatecommand=(self.register(self._validate_input), "%P"), invalidcommand=(self.register(self._handle_invalid_input), "%P"))
		btn_frame = ttk.Frame(self)
		self.up_btn = tk.Button(btn_frame, text="▲", width=2, height=1, padx=0, pady=0, font=("TkDefaultFont", 7), command = self.increment)
		self.down_btn = tk.Button(btn_frame, text="▼", width=2, height=1, padx=0, pady=0, font=("TkDefaultFont", 7), command = self.decrement)

		self.entry.grid(row = 0, column = 0, sticky = "nsew")
		btn_frame.grid(row = 0, column = 1)
		self.up_btn.grid(row = 0, column = 0)
		self.down_btn.grid(row = 1, column = 0)

	def get(self)->int:
		value = self.val.get()
		return int(value) if value not in ("", "-") else 0
	
	def set(self, value: int):
		self.val.set(str(self._clamp(value)))

	def increment(self):
		value = self.get()
		if value is None:
			value = self.min_val if self.min_val is not None else 0
		self.set(value + 1)

	def decrement(self):
		value = self.get()
		if value is None:
			value = self.min_val if self.min_val is not None else 0
		self.set(value - 1)

	def _clamp(self, value: int)->int:
		if self.min_val is not None:
			value = max(value, self.min_val)
		if self.max_val is not None:
			value = min(value, self.max_val)
		return value

	def _validate_input(self, value: str)->bool:
		if value in ("", "-"):
			return True
		try:
			v = int(value)
			if (self.min_val is not None and v < self.min_val) or (self.max_val is not None and v > self.max_val):
				return False
			return True
		except ValueError:
			return False

	def _handle_invalid_input(self, value: str):
		try:
			v = int(value)
			self.set(v)
		except ValueError:
			return