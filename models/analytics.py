import pandas as pd
from sklearn.ensemble import IsolationForest
import logging

def detect_business_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies Machine Learning (Isolation Forest) to detect anomalies or 
    outliers in business metrics for AI-driven insights.
    """
    try:
        if df is None or df.empty:
            raise ValueError("Dataframe is empty for model processing.")

        # Sirf numeric columns select kar rahe hain ML modeling ke liye
        numeric_df = df.select_dtypes(include=['number'])
        
        if numeric_df.empty:
            logging.warning("No numeric columns found for anomaly detection.")
            return df

        # Isolation Forest model initialize kar rahe hain (Industry standard for anomaly detection)
        model = IsolationForest(contamination=0.05, random_state=42)
        preds = model.fit_predict(numeric_df)

        # Results ko dataframe me add kar rahe hain
        df['anomaly_score'] = model.decision_function(numeric_df)
        df['is_anomaly'] = [True if p == -1 else False for p in preds]
        
        anomalies_count = sum(df['is_anomaly'])
        logging.info(f"Anomaly detection completed. Detected {anomalies_count} anomalies.")
        
        return df

    except Exception as e:
        logging.error(f"Error in ML analytics model: {str(e)}")
        print(f"[-] Analytics Error: {e}")
        return None