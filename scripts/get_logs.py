# scripts/get_logs.py
def check_job_status(job_uuid):
    t = get_tapis_client()
    status = t.jobs.getJobStatus(jobUuid=job_uuid)
    print(f"Current Status: {status}")
    
    if status == "FINISHED":
        # Descarga o lee los logs de salida (stdout)
        logs = t.jobs.getJobOutput(jobUuid=job_uuid, path="tapisjob.out")
        print(logs)