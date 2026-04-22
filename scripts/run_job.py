import os
from pathlib import Path
from dotenv import load_dotenv
from tapipy.tapis import Tapis

# Configuración de rutas y env
base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / '.env')

def get_tapis_client():
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=os.getenv("USERNAME"), 
            password=os.getenv("PASSWORD"))
    t.get_tokens()
    return t

def submit_test_job():
    t = get_tapis_client()
    
    # Configuración del Job mejorada
    job_def = {
        "name": "scientific-nlp-test-run",
        "appId": "scientific-nlp-dummy",
        "appVersion": "0.1.0",
        "execSystemId": "tacc.ls6.seth.v4", # CHANGE VERSION
        "description": "Prueba de ejecución desde contenedor GHCR",
        "archiveOnAppError": True,
        "parameterSet": {
            "appArgs": [
                {
                    "arg": "test_input.txt",
                    "name": "Dummy Input"
                }
            ]
        }
    }
    
    try:
        # Usamos submitJob como indica la documentación de PySDK
        result = t.jobs.submitJob(**job_def)
        print(f"🚀 Job enviado con éxito!")
        print(f"ID del Job (UUID): {result.uuid}")
        return result.uuid
    except Exception as e:
        print(f"❌ Error al enviar el Job: {e}")

if __name__ == "__main__":
    submit_test_job()