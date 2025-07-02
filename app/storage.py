import json
import os
from .models import ProcessedLead

STORAGE_DIR = "data"

def save_to_local_json(lead: ProcessedLead):
    """Guarda los datos del lead en un archivo JSON"""
    os.makedirs(STORAGE_DIR, exist_ok=True)
    file_path = os.path.join(STORAGE_DIR, f"{lead.contact_id}.json")
    
    with open(file_path, "w") as f:
        json.dump(lead.dict(), f, indent=4)