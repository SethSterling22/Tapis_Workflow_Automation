from tapipy.tapis import Tapis
import os
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env into the system environment
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'

# Carga el archivo .env especificando la ruta exacta
load_dotenv(dotenv_path=env_path)

# Access them using os.getenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def discover_and_tag():
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=username,
            password=password)
    t.get_tokens()

    print("--- Discovering Owned Apps ---")
    my_apps = t.apps.getApps()
    for app in my_apps:
        print(f"Found: {app.id} | UUID: {app.uuid}")
        
        # Register technical metadata
        meta_entry = {
            "name": "executable.provenance",
            "value": {
                "engine": "Python 3.12",
                "registry": "GHCR"
            },
            "associatedUuid": app.uuid
        }
        t.meta.createMetadata(**meta_entry)
        print(f"Metadata tagged for {app.id}")

if __name__ == "__main__":
    discover_and_tag()