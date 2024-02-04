__version__ = "v0.1.0"

from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="../.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
