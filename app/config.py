import os

from dotenv import load_dotenv

is_dotenv_loaded = load_dotenv()
print(f"Is dotenv loaded? {is_dotenv_loaded}")

DEBUG = os.getenv("DEBUG", False)
if not DEBUG:
    print("Not in debug mode")
