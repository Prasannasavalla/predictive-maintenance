# Real-Time IoT Sensor Anomaly Detection Dashboard 🏭

### Project Description
In industrial manufacturing, sudden machinery failure costs companies millions of dollars in downtime and emergency repairs. Traditional maintenance relies on fixed schedules or waiting for a machine to break down before fixing it. 

The aim of this project is to build an end-to-end streaming data pipeline that monitors high-frequency IoT sensor telemetry (like temperature) in real time. By running the incoming live data streams through an unsupervised Machine Learning model, the system automatically flags anomalies and potential machine failures instantly on an interactive web dashboard before a breakdown occurs.

---

## Tech Stack

* **Core Language:** Python 3.10
* **Machine Learning Engine:** Scikit-Learn (Isolation Forest Outlier Detection)
* **Live Web Dashboard:** Streamlit
* **Dynamic Data Visualization:** Plotly Express
* **Data Processing & Vectors:** Pandas, NumPy
* **Version Control:** Git

---

##  Key Features

* **(1)High-Frequency Stream Simulation:** Features a custom background data generator that continuously feeds live machine temperature matrices.
* **(2)Unsupervised Outlier Detection:** Utilizes an Isolation Forest model that automatically benchmarks "normal" operating conditions and catches anomalies without hardcoded manual thresholds.
* **(3)Interactive Live UI:** Implements a reactive Streamlit web dashboard that updates automatically as new data points flow into the pipeline.
* **(4)

Visual Alert Triggers:** Plots dynamic, real-time color-coded indicators (Red **X** markers) onto historical trend charts the exact second an asset spike happens.

---

## Core Process Pipeline

1. **Baseline Learning:** The AI model processes an initial history array of stable temperatures to establish a mathematical threshold for normal machine health.
2. **Telemetry Ingestion:** The live sensor loop continuously streams current operating metrics.
3. **Inference Evaluation:** The mathematical engine scores each incoming scalar value, assigning it a flag of `1` (Healthy) or `-1` (Statistical Anomaly).
4. **UI Stream Render:** The dashboard stores the current window session state, updates the rolling line chart, and triggers immediate visual warning banners if an anomaly is active.

---
Future Roadmap

This prototype works great locally, but here is how I plan to scale it for a real-world production factory:

* **Real Data Ingestion (Kafka/Redis):** Swap the Python loop for **Apache Kafka** or **Redis Streams** to handle live data streams from thousands of machinery sensors simultaneously without lag.
* **Deep Learning Upgrade (PyTorch):** Replace the Isolation Forest with a **PyTorch Autoencoder** to monitor multiple variables at once (like combining temperature, vibration, and pressure).
* **Instant Smart Alerts (Twilio/Slack):** Connect the ML engine to the **Twilio API** or Slack webhooks to automatically text the engineering team the millisecond a machine begins to fail.
* **Docker Containers:** Package the streaming script, ML backend, and Streamlit dashboard into **Docker** containers for seamless, one-click deployment to AWS or GCP.

## Cloning, Running & Executing

You can spin up this entire live monitoring dashboard on your local machine by running this single terminal block:

```bash
# 1. Clone the project workspace and navigate into it
git clone [https://github.com/prasannasavalla/predictive-maintenance.git](https://github.com/prasannasavalla/predictive-maintenance.git)
cd predictive-maintenance

# 2. Set up your local Python virtual environment sandbox
python -m venv venv

# 3. Activate your virtual environment
# Windows Command Prompt:
venv\Scripts\activate.bat
# Windows PowerShell:  .\venv\Scripts\activate.ps1
# macOS / Linux:       source venv/bin/activate

# 4. Install all required data engineering and ML dependencies
pip install -r requirements.txt

# 5. Launch the live real-time AI anomaly detection web application!
streamlit run app.py
