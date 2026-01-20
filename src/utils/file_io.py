import json
import os

def save_json(data, filepath):
   
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Saved JSON to {filepath}")

def load_json(filepath):
    
    with open(filepath, "r") as f:
        data = json.load(f)
    return data
