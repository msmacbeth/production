from dotenv import load_dotenv
import os
from data_manager import DataManager

# Load variables from the .env file
load_dotenv()

# Verify paths are correct
print("PRICE_DATA:", os.getenv("PRICE_DATA"))
print("FEATURES_DATA:", os.getenv("FEATURES_DATA"))
print("TICKERS:", os.getenv("TICKERS"))

# Check all necessary variables are set
if not all([os.getenv("PRICE_DATA"), os.getenv("FEATURES_DATA"), os.getenv("TICKERS")]):
    raise ValueError("One or more environment variables are not set. Check your .env file.")

# Initialize DataManager with date range
data_manager = DataManager(
    start_date="2000-01-01",
    end_date="2023-12-31"
)
print("DataManager initialized.")

# Download and Save All Price Data
data_manager.download_all()
print("Data download completed.")

# Load Prices and Create Features
data_manager.featurize()
print("Feature engineering completed.")