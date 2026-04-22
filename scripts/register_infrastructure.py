import json
import argparse
from tapipy.tapis import Tapis
from dotenv import load_dotenv

# Load variables from .env into the system environment
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'

# Carga el archivo .env especificando la ruta exacta
load_dotenv(dotenv_path=env_path)

# Access them using os.getenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def get_tapis_client():
    # Use your TACC credentials here
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=username,
            password=password)
    t.get_tokens()
    return t

def register_app(t):
    with open('apps/translator-app/app-definition.json', 'r') as f:
        app_def = json.load(f)
    t.apps.createApp(**app_def)
    print(f"Successfully registered App: {app_def['id']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tapis Infrastructure Automator")
    parser.add_argument('--type', choices=['app'], required=True)
    args = parser.parse_args()

    client = get_tapis_client()
    if args.type == 'app':
        register_app(client)
    print(f"Successfully authenticated as: {username}")
