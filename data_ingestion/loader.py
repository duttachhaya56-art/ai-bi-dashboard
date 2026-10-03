import pandas as pd
import logging
import os

# Error tracking ke liye logs folder ensure kar rahe hain
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(file_path: str) -> pd.DataFrame:
    """
    Securely loads dataset with robust error handling for production resilience.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target file not found at: {file_path}")
        
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data from {file_path}. Shape: {df.shape}")
        return df

    except Exception as e:
        logging.error(f"Error during data ingestion: {str(e)}")
        print(f"[-] Error loading data: {e}")
        return None