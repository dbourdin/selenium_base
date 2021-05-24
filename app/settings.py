import os

from dotenv import load_dotenv


load_dotenv()

WAIT_TIMEOUT = 40
HEADLESS = os.getenv("RUN_HEADLESS", False)
