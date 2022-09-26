import os
from py_dotenv import read_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
read_dotenv(dotenv_path)

# Get api keys
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_API_END_POINT = os.getenv("STOCK_API_END_POINT")
ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD"))