# Tapis Workflow Automation: NL to Scientific Language

## Overview
This project provides a robust framework for automating scientific workflows using **Tapis v3**. It bridges the gap between **Natural Language (NL)** instructions and **Scientific Language (SL)** execution by leveraging containerized NLP engines orchestrated through Tapis Workflows and Pipelines.

## Infrastructure Architecture
- **Orchestration:** Tapis Workflows (DAG-based execution).
- **Execution:** Tapis Apps running on TACC HPC systems (e.g., Frontera, Lonestar6).
- **Runtime:** Docker/Singularity for environment consistency.
- **Metadata:** Tapis Meta service for resource discovery and provenance tracking.

## Project Structure
- `apps/`: Contains the Tapis App definitions and Docker recipes for the scientific engines.
- `workflows/`: Defines the logical flow and task dependencies of the pipeline.
- `scripts/`: Python automation scripts using `tapipy` for infrastructure-as-code (IaC) management.

```
tapis_workflow_automation
├── .env
├── .gitignore
|
├── .github/
│   └── workflows/
│       └── docker-publish.yml
|
├── apps/
│   └── translator-app/
│       ├── app-definition.json
│       ├── Dockerfile
│       └── hello_world.py
|
├── scripts/
│   ├── register_infrastructure.py
│   └── discover_resources.py
|
├── requirements.txt
└── README.md
```


## Setup & Registration

### Prerequisites
- Python 3.12+
- Access to a Tapis v3 Tenant (e.g., TACC)
- Docker installed

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/SethSterling22/tapis_workflow_automation.git](https://github.com/SethSterling22/tapis_workflow_automation.git)

2. Create a virtual environment and install dependencies:

```Bash
python3 -m venv tapis-env
source tapis-env/bin/activate
pip install tapipy setuptools<70
```

3. Registering the App
Run the registration script to deploy the App definition to the Tapis service:

```Bash
python3 scripts/register_infrastructure.py --type app
````


Deploying the Workflow
Register the combined pipeline:

```Bash
python3 scripts/register_infrastructure.py --type workflow
```

Resource Discovery
To discover and audit all tasks and pipelines associated with your account, use the discovery utility:

```Bash
python3 scripts/discover_resources.py --owner your_username
```

### License
MIT License


