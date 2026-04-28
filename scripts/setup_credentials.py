import os
from pathlib import Path
from dotenv import load_dotenv
from tapipy.tapis import Tapis

base_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=base_path / '.env')

def setup_system_credentials():
    t = Tapis(base_url='https://tacc.tapis.io', 
            username=os.getenv("USERNAME"), 
            password=os.getenv("PASSWORD"))
    t.get_tokens()

    system_id = "tacc.ls6.seth.v10" # CHANGE VERSION
    
    print(f"--- Configurando credenciales para {system_id} ---")
    
    try:
        # Registramos las credenciales para que Tapis pueda hacer SSH/SFTP
        t.systems.createUserCredential(
            systemId=system_id,
            userName=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD")
        )
        print("✅ Credenciales vinculadas exitosamente.")
    except Exception as e:
        print(f"❌ Error al configurar credenciales: {e}")

if __name__ == "__main__":
    setup_system_credentials()