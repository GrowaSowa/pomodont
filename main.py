import modules.config
from modules.app import App

if __name__ == "__main__":
	app = App()
	app.mainloop()
	app.save_config_to_file()
