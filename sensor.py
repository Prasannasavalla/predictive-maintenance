import time
import random

def generate_sensor_reading(step):
    # Standard normal operating temperature
    base_temperature = 70.0
    noise = random.uniform(-2.0, 2.0)
    current_temp = base_temperature + noise
    
    # Force a fake "malfunction spike" every 15 steps to simulate an anomaly
    if step % 15 == 0 and step > 0:
        current_temp += random.uniform(50.0, 70.0)
        print(f"[⚠️ FACTORY ALERT] Step {step}: Machine is overheating!")
        
    return round(current_temp, 2)

# Run a simple loop to test our data stream
print("Starting live machinery sensor stream... Press Ctrl+C to stop.")
step = 0
try:
    while True:
        temp = generate_sensor_reading(step)
        print(f"Step {step:02d} -> Machine Temperature: {temp}°C")
        step += 1
        time.sleep(1) # Wait 1 second before reading the sensor again
except KeyboardInterrupt:
    print("\nStream stopped gracefully.")