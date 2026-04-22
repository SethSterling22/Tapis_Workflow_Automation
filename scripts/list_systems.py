import os
from pathlib import Path
from dotenv import load_dotenv
from tapipy.tapis import Tapis

base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / '.env')

def list_my_systems():
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=os.getenv("USERNAME"), 
            password=os.getenv("PASSWORD"))
    t.get_tokens()
    
    print("--- Sistemas de Ejecución Disponibles ---")
    systems = t.systems.getSystems()
    if not systems:
        print("No se encontraron sistemas. ¡Debes registrar uno!")
    for s in systems:
        print(f"ID: {s.id} | Tipo: {s.systemType} | Host: {s.host}")

if __name__ == "__main__":
    list_my_systems()