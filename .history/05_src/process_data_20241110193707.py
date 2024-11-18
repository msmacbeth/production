from dotenv import load_dotenv
import os

# Load variables
load_dotenv()

# Verify paths 
if not all([os.getenv("PRICE_DATA"), os.getenv("FEATURES_DATA"), os.getenv("TICKERS")]):
    raise ValueError("One or more environment variables are not set. Check your .env file.")

from data_manager import DataManager
from dotenv import load_dotenv
import os

load_dotenv()

# Verify that the paths are loaded correctly
print("PRICE_DATA:", os.getenv("PRICE_DATA"))
print("FEATURES_DATA:", os.getenv("FEATURES_DATA"))
print("TICKERS:", os.getenv("TICKERS"))

# Initialize DataManager and run steps
data_manager = DataManager(
    start_date="2000-01-01",
    end_date="2023-12-31"
)
print("DataManager initialized.")

# Step 1: Download and Save All Price Data
data_manager.download_all()
print("Data download completed.")

# Step 2: Load Prices and Create Features
data_manager.featurize()
print("Feature engineering completed.")

