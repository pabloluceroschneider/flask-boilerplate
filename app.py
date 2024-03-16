import os
from src import app
from config import config

if __name__ == "__main__":
    scope_config = config[os.getenv("CONFIG_MODE")]

    app.config.from_object(scope_config)
    
    app.run()