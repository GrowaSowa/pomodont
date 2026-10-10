import modules.config
from modules.app import App

if __name__ == "__main__":
	app = App()
	app.mainloop()

	modules.config.save_config("config.json", app.config)
