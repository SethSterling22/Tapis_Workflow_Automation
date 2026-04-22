import json
import argparse
from tapipy.tapis import Tapis
import os
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env into the system environment
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'

# Carga el archivo .env especificando la ruta exacta
load_dotenv(dotenv_path=env_path)

def get_tapis_client():
    # Use your TACC credentials here
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=os.getenv("USERNAME"), 
            password=os.getenv("PASSWORD"))
    t.get_tokens()
    return t

def register_app(t):
    with open('apps/translator_app/app_definition.json', 'r') as f:
        app_def = json.load(f)

    try:
        t.apps.createAppVersion(**app_def)
        print(f"Successfully registered App: {app_def['id']} version {app_def['version']}")
    except Exception as e:
        print(f"Registration failed: {e}")

def register_system(t):
    with open('systems/ls6-system.json', 'r') as f:
        sys_def = json.load(f)
    
    system_id = sys_def['id']
    try:
        # Intentamos crearlo
        t.systems.createSystem(**sys_def)
        print(f"✅ Sistema registrado con éxito: {system_id}")
    except Exception as e:
        if "SYSAPI_SYS_EXISTS" in str(e):
            print(f"🔄 El sistema {system_id} ya existe. Actualizando configuración...")
            # En Tapis v3, para actualizar un sistema completo se usa putSystem
            t.systems.putSystem(systemId=system_id, **sys_def)
            print(f"✅ Sistema {system_id} actualizado correctamente con host .edu")
        else:
            print(f"❌ Error inesperado: {e}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tapis Infrastructure Automator")
    parser.add_argument('--type', choices=['app', 'system'], required=True)
    args = parser.parse_args()

    client = get_tapis_client()
    if args.type == 'system':
        register_system(client)
    elif args.type == 'app':
        register_app(client)
    print(f"Successfully authenticated as: {os.getenv("USERNAME")}")
