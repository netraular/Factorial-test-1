import json
import os

STORAGE_DIR = "data"

def save_to_local_json(lead_data: dict):
    """Guarda los datos del lead en un archivo JSON"""
    os.makedirs(STORAGE_DIR, exist_ok=True)
    
    contact_id = lead_data.get("contact_id", "unknown_contact")
    file_path = os.path.join(STORAGE_DIR, f"{contact_id}.json")

    with open(file_path, "w") as f:
        json.dump(lead_data, f, indent=4)