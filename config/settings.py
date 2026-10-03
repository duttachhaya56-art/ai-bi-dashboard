import os
from dotenv import load_dotenv

# Environment variables load kar rahe hain
load_dotenv()

class Settings:
    PROJECT_NAME = "AI Business Intelligence Dashboard"
    VERSION = "1.0.0"
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

settings = Settings()