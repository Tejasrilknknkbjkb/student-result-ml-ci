
import json
import os
import sys

if not os.path.exists("metrics.json"):
    print("ERROR: metrics.json not found. Train the model first.")
    sys.exit(1)

with open("metrics.json", "r") as file:
    metrics = json.load(file)

accuracy = metrics.get("accuracy", 0)

print("Model Accuracy:", accuracy)

if accuracy >= 0.70:
    print("QUALITY GATE PASSED")
else:
    print("QUALITY GATE FAILED")
    sys.exit(1)
