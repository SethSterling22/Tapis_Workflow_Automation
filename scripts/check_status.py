import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from tapipy.tapis import Tapis

# 1. Configuración de rutas y carga de credenciales
base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / '.env')

def get_tapis_client():
    try:
        t = Tapis(base_url='https://tacc.tapis.io', 
                username=os.getenv("USERNAME"), 
                password=os.getenv("PASSWORD"))
        t.get_tokens()
        return t
    except Exception as e:
        print(f"❌ Error de autenticación: {e}")
        sys.exit(1)

def monitor_job(job_uuid):
    t = get_tapis_client()
    
    try:
        # Obtenemos los detalles del job
        job = t.jobs.getJob(jobUuid=job_uuid)
        
        print("\n" + "="*30)
        print(f"STATUS REPORT: {job.name}")
        print("="*30)
        print(f"UUID:   {job.uuid}")
        print(f"Estado: {job.status}")
        print(f"Mensaje: {job.lastMessage}")
        print(f"Sistema: {job.execSystemId}")
        print("="*30)

        # Si el job terminó, mostramos dónde están los resultados
        if job.status == "FINISHED":
            print(f"✅ El trabajo ha finalizado con éxito.")
            print(f"📁 Directorio de salida: {job.archiveSystemDir}")
        elif job.status == "FAILED":
            print(f"❌ El trabajo falló. Revisa los logs para más detalles.")
            
    except Exception as e:
        print(f"❌ Error al consultar el Job: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        monitor_job(sys.argv[1])
    else:
        print("⚠️  Uso: python scripts/check_status.py <JOB_UUID>")