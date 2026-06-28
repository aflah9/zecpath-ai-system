from ai_core.performance_optimized import batch_resume_processing

def process_resume(resume):
    return {
        "resume": resume,
        "status": "Processed"
    }

resumes=[
    "resume1.pdf",
    "resume2.pdf",
    "resume3.pdf",
    "resume4.pdf"
]

results=batch_resume_processing(resumes,process_resume)

for r in results:
    print(r)
    