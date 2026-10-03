An enterprise-grade, interactive Business Intelligence (BI) dashboard built with Python, Streamlit, and Machine Learning. This application is designed to empower executives and data analysts with automated anomaly detection, real-time exploratory data analysis (EDA), and actionable business insights.

🌟 Key Features
🤖 Automated Anomaly Detection: Utilizes an unsupervised Machine Learning model (Isolation Forest) to scan transactional records and flag potential financial or operational risks.

📊 Dynamic Data Exploration: Interactive filtering and metric selection allowing users to visualize trends using dynamic scatter plots, line charts, and custom data breakdowns.

📋 Executive Summary Reports: Instantaneous audit reporting that summarizes total transaction volume, detected risk anomalies, and critical business metrics at a glance.

📥 Export Capabilities: Cleaned and analyzed dataset export functionality enabling users to download processed reports directly in CSV format.

🔒 Enterprise Security: Built with strict environment isolation and secure configuration management to protect sensitive data assets.

🛠️ Tech Stack
Frontend & UI: Streamlit

Data Processing & Manipulation: Pandas, NumPy

Machine Learning: Scikit-learn (Isolation Forest)

Data Visualization: Streamlit Native Charts, Matplotlib / Seaborn
📂 Project Architecture
Plaintext
ai-bi-dashboard/
│
├── config/
│   └── settings.py          # Configuration parameters and application constants
├── dashboard/
│   └── app.py               # Main Streamlit application entry point
├── data_ingestion/
│   └── loader.py            # Data loading and ingestion pipelines
├── models/
│   └── analytics.py         # Isolation Forest anomaly detection engine
├── processing/
│   └── transformer.py       # Data cleaning, transformation, and sampling logic
├── .gitignore               # Excludes sensitive and temporary artifacts
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
⚙️ Installation & Setup
Follow these steps to run the project locally on your machine:

Clone the Repository:

Bash
git clone https://github.com/duttachhaya56-art/ai-bi-dashboard.git
cd ai-bi-dashboard
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Streamlit Application:

Bash
python -m streamlit run dashboard/app.py
