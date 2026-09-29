import json
import os

DATA_PATH = os.path.join("..", "data", "ipc.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total records:", len(data))
print("\nFirst record structure:\n")
print(data[0])
