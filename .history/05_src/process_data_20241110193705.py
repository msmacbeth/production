from dotenv import load_dotenv
import os

# Load variables
load_dotenv()

# Verify paths 
if not all([os.getenv("PRICE_DATA"), os.getenv("FEATURES_DATA"), os.getenv("TICKERS")]):
    raise ValueError("One or more environment variables are not set. Check your .env file.")


