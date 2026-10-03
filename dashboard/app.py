import streamlit as st
import pandas as pd
import os

#apne modular components ko import kar rahe hain
from data_ingestion.loader import load_data
from processing.transformer import clean_and_transform_data
from models.analytics import detect_business_anomalies

# page configuration
st.set_page_config(
    page_title = "AI Business Intelligence Dashboard",
    page_icon = "📊",
    layout = "wide"

)

st.title("🚀 AI-Powered Business Intelligence & Analytics Dashboard")
st.markdown("---")

#Sidebar for controls
st.sidebar.header("📁 Data Source Configuration")
uploaded_file = st.sidebar.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    # Temporary save krke load kr rhe hain
    temp_path = "temp.csv"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        with st.spinner("🔄 Loading and processing data through pipeline..."):
            # 1. Ingestion
            raw_df = load_data(temp_path)
        
        if raw_df is not None:
            # 2. Transformation
            clean_df = clean_and_transform_data(raw_df)
            
            # 3. AI Analytics
            final_df = detect_business_anomalies(clean_df)
            st.success("✨ Pipeline executed successfully!")

            # Metrics display
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", final_df.shape[0])
            col2.metric("Total Columns", final_df.shape[1])
            if 'is_anomaly' in final_df.columns:
                anomalies_count = int(final_df['is_anomaly'].sum())
                col3.metric("AI Detected Anomalies", anomalies_count, delta_color="inverse")
# Visual Analytics & Charts Section
            st.markdown("---")
            st.subheader("📈 Impactful Business Insights & Trends")
            
            numeric_cols = final_df.select_dtypes(include=['number']).columns.tolist()
            if len(numeric_cols) >= 2:
                col_x = st.selectbox("Select X-axis metric:", numeric_cols, index=0)
                col_y = st.selectbox("Select Y-axis metric:", numeric_cols, index=1)
                st.line_chart(final_df[[col_x, col_y]].head(1000))
            
            # Executive Summary Report
            st.markdown("### 📋 Executive Summary Report")
            total_records = final_df.shape[0]
            anomalies_detected = int(final_df['is_anomaly'].sum()) if 'is_anomaly' in final_df.columns else 0
            
            st.info(
                f"**Audit Report:** Out of **{total_records}** total transactions analyzed, "
                f"the AI model successfully isolated **{anomalies_detected}** potential risk anomalies "
                f"requiring immediate business review."
            )
            st.markdown("---")
            st.subheader("🔍 Processed Data Preview")
            st.dataframe(final_df.head(10))

            # Download processed data
            csv_data = final_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Cleaned & Analyzed Data",
                data=csv_data,
                file_name="ai_bi_processed_data.csv",
                mime="text/csv"
            )
            
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)
        else:
            st.error("❌ Failed to process the dataset. Check logs/app.log for details.")
else:
    st.info("👈 Kripya sidebar se apna CSV dataset upload karein dashboard shuru karne ke liye!")