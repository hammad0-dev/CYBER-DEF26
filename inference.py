import pandas as pd
import joblib
import os
import time
# Load trained model
model = joblib.load("model.pkl")

# Input file
input_file = "/input/logs/logs.csv"

# Output file
output_file = "/output/alerts.csv"

# Check if input exists
if not os.path.exists(input_file):
    print(f"Input file not found: {input_file}")
    exit()

# Read logs
logs = pd.read_csv(input_file)

# Select required features
X = logs[['duration', 'src_bytes', 'dst_bytes']]

# Predict malware/threats
predictions = model.predict(X)

# Add predictions to logs
logs['threat_detected'] = predictions

# Save output
logs.to_csv(output_file, index=False)

print("Inference completed successfully.")
print(f"Alerts saved to: {output_file}")

print("Container will stay alive for monitoring...")

while True:
    time.sleep(60)
