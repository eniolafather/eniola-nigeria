def match_job_to_workers(job_description: dict, workers_db: list, jobs_db: list) -> list:
    """
    Queries workers and jobs tables based on location, skills, and budget constraints.
    
    NOTE: This is a placeholder implementation simulating DB interaction.
    It expects job_description to contain 'location', 'skills' (list), and 'budget'.
    It expects workers to have 'location', 'skills' (list), and 'rate'.
    """
    
    required_location = job_description.get('location')
    required_skills = set(job_description.get('skills', []))
    # Budget is treated as the max acceptable rate for a worker in this placeholder
    max_budget = job_description.get('budget', float('inf'))
    
    potential_workers = []
    
    for worker in workers_db:
        # 1. Location check
        if required_location and worker.get('location') != required_location:
            continue
            
        # 2. Skills check (must have ALL required skills)
        worker_skills = set(worker.get('skills', []))
        if not required_skills.issubset(worker_skills):
            continue
            
        # 3. Budget check
        worker_rate = worker.get('rate', 0)
        if worker_rate > max_budget:
            continue
            
        potential_workers.append(worker)
        
    return potential_workers