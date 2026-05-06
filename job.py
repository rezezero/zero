def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    slots = [False] * len(jobs)
    
    print("Scheduled Jobs:")
    
    for job in jobs:
        for j in range(min(len(jobs), job[2]) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                print(job[0])
                break

jobs = [
    ("A",100,2),
    ("B",19,1),
    ("C",27,2),
    ("D",25,1),
    ("E",15,3)
]

job_scheduling(jobs)