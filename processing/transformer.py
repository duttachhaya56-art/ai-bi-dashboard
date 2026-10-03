import pandas as pd
import logging

def clean_and_transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans dataset by handling missing values and formatting columns 
    for enterprise-grade business intelligence.
    """
    try:
        if df is None or df.empty:
            raise ValueError("Input dataframe is empty or None.")

        # Duplicate rows remove kar rahe hain
        initial_count = len(df)
        df = df.drop_duplicates()
        logging.info(f"Removed {initial_count - len(df)} duplicate rows.")

        # Numeric columns ke missing values ko median se fill kar rahe hain (robust approach)
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                logging.info(f"Filled missing values in column '{col}' with median: {median_val}")

        logging.info("Data transformation completed successfully.")
        return df

    except Exception as e:
        logging.error(f"Error during data transformation: {str(e)}")
        print(f"[-] Transformation Error: {e}")
        return None