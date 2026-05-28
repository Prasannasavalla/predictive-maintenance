import time
import random
import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Reuse our trusty sensor simulator function
def generate_sensor_reading(step):
    base_temperature = 70.0
    noise = random.uniform(-2.0, 2.0)
    current_temp = base_temperature + noise
    if step % 15 == 0 and step > 0:
        current_temp += random.uniform(50.0, 70.0)
    return round(current_temp, 2)

print("🧠 Pre-training AI brain on normal factory conditions...")
# Collect 30 normal baseline readings so the AI knows what 'good' looks like
history = [[generate_sensor_reading(i)] for i in range(1, 31)]

# Initialize and train our Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(history)
print("✅ Training complete. AI now understands normal operations!\n")

print("🚀 Starting Live Monitoring Loop...")
step = 0
try:
    while True:
        # Get live reading and reshape it for the model
        temp = generate_sensor_reading(step)
        temp_array = np.array([[temp]])
        
        # Ask the AI to predict: 1 = Normal, -1 = Anomaly
        prediction = model.predict(temp_array)[0]
        
        # Display the result with its AI status label
        if prediction == -1:
            status = "🚨 ANOMALY DETECTED BY AI!"
        else:
            status = "🟢 Normal"
            
        print(f"Step {step:02d} | Temp: {temp}°C | Status: {status}")
        
        step += 1
        time.sleep(0.8) # Slightly faster processing speed
        
except KeyboardInterrupt:
    print("\nAI engine stopped gracefully.")