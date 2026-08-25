import json
import os
from dataclasses import dataclass, asdict

@dataclass
class AppConfig:
	session_time: tuple[int, int, int] = (0, 25, 0)
	break_time: tuple[int, int, int] = (0, 5, 0)
	n_sessions: int = 4
	session_bar_color: str = "blue"
	break_bar_color: str = "green"
	pause_bar_color: str = "grey"
	session_end_sound: str = "D:\\backup_new\\music\\effects\\aughhh.mp3"
	break_end_sound: str = "D:\\backup_new\\music\\effects\\quack.mp3"

def load_config(fname: str)->AppConfig:
	if(os.path.exists(fname)):
		with open(fname, "r") as f:
			cfg = json.load(f)
		return AppConfig(**cfg)
	else:
		return AppConfig()

def save_config(fname: str, config: AppConfig):
	with open(fname, "w") as f:
		f.write(json.dumps(asdict(config)))
