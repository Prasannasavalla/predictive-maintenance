import streamlit as pd_st
import streamlit as st
import time
import random
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="IoT Predictive Maintenance", layout="wide")
st.title("🏭 Real-Time IoT Sensor Anomaly Detection Dashboard")
st.markdown("This AI system monitors machine temperature and automatically flags anomalies using an *Isolation Forest* model.")

# --- 1. SENSOR SIMULATOR ---
def generate_sensor_reading(step):
    base_temperature = 70.0
    noise = random.uniform(-2.0, 2.0)
    current_temp = base_temperature + noise
    if step % 15 == 0 and step > 0:
        current_temp += random.uniform(50.0, 70.0)
    return round(current_temp, 2)

# --- 2. INITIAL AI TRAIN ---
@st.cache_resource
def train_ai_model():
    # Train on a clean baseline
    history = [[random.uniform(68.0, 72.0)] for _ in range(50)]
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(history)
    return model

ai_brain = train_ai_model()

# --- 3. LIVE STREAM LAYOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Live Temperature Telemetry Stream")
    chart_placeholder = st.empty()

with col2:
    st.subheader("🚨 Real-Time System Alerts")
    alert_placeholder = st.empty()

# Persistent list to store stream data for plotting
if "df_data" not in st.session_state:
    st.session_state.df_data = pd.DataFrame(columns=["Step", "Temperature", "Status"])

# Run the live browser engine loop
step = len(st.session_state.df_data)

# Simple button to turn the machine monitoring on
start_monitoring = st.checkbox("🔌 Run Industrial Machinery Stream", value=True)

if start_monitoring:
    while True:
        temp = generate_sensor_reading(step)
        
        # ML Inference
        pred = ai_brain.predict(np.array([[temp]]))[0]
        status = "Anomaly" if pred == -1 else "Normal"
        
        # Save new data point to session state
        # REPLACE IT WITH THIS:
        new_row = pd.DataFrame([{"Step": int(step), "Temperature": float(temp), "Status": str(status)}])
        st.session_state.df_data = pd.concat([st.session_state.df_data, new_row], ignore_index=True).astype({"Step": int, "Temperature": float, "Status": str})
        
        # Keep only the last 40 data points on screen so it scrolls smoothly
        display_df = st.session_state.df_data.tail(40)
        
        # Create a beautiful dynamic color-coded plot
        fig = px.line(display_df, x="Step", y="Temperature", title="Machinery Thermal State")
        fig.add_scatter(x=display_df[display_df["Status"] == "Anomaly"]["Step"], 
                        y=display_df[display_df["Status"] == "Anomaly"]["Temperature"],
                        mode='markers', name='AI Detected Anomaly', 
                        marker=dict(color='red', size=12, symbol='x'))
        
        # REPLACE IT WITH THIS:
        chart_placeholder.plotly_chart(fig, width="stretch")
        
        # Update our Live Alert Window
        with alert_placeholder.container():
            if status == "Anomaly":
                st.error(f"⚠️ CRITICAL OUTLIER DETECTED!\n\nStep {step}: Machine spike at {temp}°C!")
            else:
                st.success(f"🟢 System Healthy\n\nCurrent Temp: {temp}°C")
        
        step += 1
        time.sleep(0.7)