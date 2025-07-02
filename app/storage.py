import json
import os

def save_to_local_json(lead_data: dict):
    """Guarda los datos del lead en un archivo JSON"""
    os.makedirs("data", exist_ok=True)
    filename = f"data/{lead_data['contact_id']}.json"
    
    with open(filename, 'w') as f:
        json.dump(lead_data, f)