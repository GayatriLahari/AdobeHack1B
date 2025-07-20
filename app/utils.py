import os
import json
from datetime import datetime

def save_json(data, path):
    """Save a Python object as JSON."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_json(path):
    """Load JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def get_current_timestamp():
    """Get ISO-format timestamp."""
    return datetime.now().isoformat()

def list_pdfs(directory):
    """Return list of .pdf files in a directory."""
    return [f for f in os.listdir(directory) if f.endswith(".pdf")]
