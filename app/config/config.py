from pathlib import Path
from dotenv import load_dotenv
import os


env_path = Path(__file__).resolve().parent.parent.parent / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    def __init__(self):
        self.flag = os.getenv('FLAG')

settings = Settings()
