import os

dataset_path = r"C:\Users\AA\.cache\kagglehub\datasets\adarshsingh0903\legal-dataset-sc-judgments-india-19502024\versions\1"

for root, dirs, files in os.walk(dataset_path):
    print("\nFOLDER:", root)
    for f in files:
        print("  -", f)