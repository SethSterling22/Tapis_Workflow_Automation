from tapipy.tapis import Tapis
from dotenv import load_dotenv

# Load variables from .env into the system environment
load_dotenv()

# Access them using os.getenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# 1. Authenticate to TACC
t = Tapis(base_url='https://tacc.tapis.io', username='YOUR_USER', password='YOUR_PASSWORD')
t.get_tokens()

# 2. Define the App
# This app runs a containerized python script as a Tapis Job
app_def = {
    "id": "scientific-nlp-translator",
    "version": "0.1.0",
    "description": "Task to handle data and feedback: NL to Scientific Language",
    "containerImage": "docker://sethsterling22/scientific-nlp:latest",
    "jobType": "FORK",
    "runtime": "DOCKER",
    "executionSystemId": "tacc.ls6.seth", // Target execution system
    "jobAttributes": {
        "description": "NLP translation task",
        "parameterSet": {
            "appArgs": [
                {
                    "arg": "input_query.txt",
                    "name": "Input Query File"
                }
            ]
        }
    }
}

# 3. Register the App
t.apps.createApp(**app_def)
print("App registered successfully!")
