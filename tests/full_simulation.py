


from ai_engines.ats_scorer import ats_score_engine
from ai_engines.fairness_engine import fairness_pipeline

from screening_ai.scoring_engine import screening_scoring_pipeline

from interview_ai.hr_scoring_engine import hr_scoring_pipeline

from technical_ai.technical_scoring_engine import calculate_technical_score

from machine_test.pipeline import machine_test_pipeline

from integrity_ai.integration import combined_risk

from integrity_ai.main import evaluate_integrity

from ai_core.hiring_fit import calculate_hiring_fit

from ai_core.decision_engine import generate_decision

from ai_engines.resume_text_extractor import ResumeTextExtractor

from ai_engines.jd_parser import parse_job_description

import spacy

#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_md")
import os
import json
import random
#mock data for 56


intent_map = {
    "Q1": "experience"
}

responses = [
    {
        "question_id":"Q1",
        "answer": random.choice([
            "I have strong communication skills",
            "I have led finance teams",
            "I work well under pressure",
            "I am passionate about credit analysis"
        ]),
        "tone":"confident",
        "category":"experience"
        },
    
        {
        "question_id": "Q2",
        "answer": "I communicate well with teams",
        "tone": "neutral",
        "category": "communication"
    }
]


technical_answers = [
    "REST APIs allow communication between systems",
    "Python supports OOP and asynchronous programming",
    "DSCR measures debt repayment capacity",
    "Financial statement analysis helps assess creditworthiness"
]

candidate_answer = random.choice(technical_answers)

candidate_data = {
    "task_score": 80
}
import random
events = {
    "voice_detect":  random.randint(0, 1),
    "tab_switch": random.randint(0, 5),
    "gaze_off": random.randint(0, 8),
    "gaze_deviation":random.randint(0,10),
    "mouse_away": random.randint(0, 5),
    "face_missing": random.randint(0, 8),
    "focus_loss": random.randint(0, 3)
}
#started here


def simulate_candidate(candidate_id, resume_data):


    print(type(resume_data))
    print(resume_data)

    print(json.dumps(resume_data, indent=2))

    # ATS
     
    extractor = ResumeTextExtractor()

    jd_text = extractor.extract_text(
    "sample_data/job_description.pdf"
    )

    jd_data = parse_job_description(jd_text)

    ats_resume_data = {
    "skills": resume_data["basic_info"].get("skills", []),
    "experience_years": resume_data["basic_info"].get("experience_years", "0"),
    "education": resume_data["basic_info"].get("education", "")
}
    ats_resume_data = {
    "skills": resume_data["basic_info"].get("skills", []),

    "experience": resume_data["basic_info"].get(
        "experience_years",
        f"{random.randint(0,10)} years"
    ),

    "education": resume_data["basic_info"].get(
        "education",
        ""
    ),

    "text": json.dumps(resume_data)
}
    print("\nJD DATA")
    print(jd_data)

    ats_result = ats_score_engine(
        ats_resume_data,
        jd_data,
        nlp
    )

    ats_score = ats_result["final_score"]

    # Screening
    import inspect

    print(screening_scoring_pipeline)
    print(inspect.signature(screening_scoring_pipeline))
    experience_years = resume_data["basic_info"].get(
    "experience_years",
    f"{random.randint(0,10)} years"
)



    answers = [
        {
            "question_id": "Q1",
            "answer": f"I have {experience_years} experience in credit analysis",
            "intent": "experience"
        }
    ]

    print("ANSWERS:")
    print(answers)
    print(type(answers))

    screening_result = screening_scoring_pipeline(
    answers,
    intent_map
)
    print(screening_result)

    screening_score = screening_result.get("final_score",0)
    print("SCREENING SCORE:", screening_score)

    # HR
    import inspect

    print(hr_scoring_pipeline)
    print(inspect.signature(hr_scoring_pipeline)
          )
    hr_result = hr_scoring_pipeline(
    answers,
    candidate_type="fresher"
)
    print(hr_result)

    hr_score = hr_result["hr_score"]

    # Technical
    technical_result = calculate_technical_score(
        candidate_answer,
        is_correct=True
    )

    technical_score = technical_result["technical_score"]

    # Machine Test
    machine_test_data = {
    "candidate_id": candidate_id,

    "execution_results": {
        "passed": 8,
        "total": 10,
        "runtime": 18
    },

    "code_snapshot": "def solve(): return True",

    "attempts": 2,

    "time_taken": 22
}
    machine_result = machine_test_pipeline(
        machine_test_data
    )

    machine_test_score = machine_result["final_score"]

    # Integrity
    integrity_result = evaluate_integrity(
        candidate_id=candidate_id,
        events=events
    )

    integrity_risk = integrity_result["risk_level"]

    # Final Score
    final_score = round(
        (
            ats_score +
            screening_score +
            hr_score +
            technical_score +
            machine_test_score
        ) / 5,
        2
    )

    # Hiring Fit
    fit_result = calculate_hiring_fit(final_score)
#debug prints
    print("="*50)
    print("CANDIDATE:", candidate_id)

    print("ATS SCORE:", ats_score)
    print("SCREENING:", screening_score)
    print("HR:", hr_score)
    print("TECHNICAL:", technical_score)
    print("MACHINE:", machine_test_score)
    print("INTEGRITY:", integrity_result)

    print("RESUME DATA")
    print(json.dumps(resume_data, indent=2))
    # Decision
    print("\n===== DECISION INPUT =====")
    print("Final Score:", final_score)
    print("Technical:", technical_score)
    print("Behavior:", "Low Risk")
    print("Integrity:", integrity_risk)

    decision_result = generate_decision(
        final_score=final_score,
        technical_score=technical_score,
        behavior_risk="Low Risk",
        integrity_risk=integrity_risk
    )

    return {
        "candidate_id": candidate_id,
        "candidate_name": resume_data["basic_info"].get("name", "Unknown"),
        "role": resume_data["experience_analysis"].get("target_role", ""),
        "ats": ats_score,
        "screening": screening_score,
        "hr": hr_score,
        "technical": technical_score,
        "machine_test": machine_test_score,
        "integrity": integrity_risk,
        "final_score": final_score,
        "decision": decision_result["decision"]
    }

def run_full_simulation():

    resume_folder = "sample_resumes"

    resume_files = [
        f for f in os.listdir(resume_folder)
        if f.lower().endswith(".pdf")
    ]

    results = []

    for index, file in enumerate(resume_files, start=1):

        candidate_id = f"C{20000 + index}"

        json_file = os.path.join(
            "outputs",
            f"{file}_final.json"
        )

        print("Loading:", json_file)

        if not os.path.exists(json_file):
            print("JSON not found:", json_file)
            continue

        with open(json_file, "r", encoding="utf-8") as f:
            resume_data = json.load(f)

        result = simulate_candidate(
            candidate_id,
            resume_data
        )

        results.append(result)

    return results

if __name__ == "__main__":

    results = run_full_simulation()

    print(f"\nTotal Candidates Processed: {len(results)}")

    selected = 0
    rejected = 0

    selected = [r for r in results if r["decision"] == "Selected"]
    rejected = [r for r in results if r["decision"] == "Rejected"]
    
    print("\n=====" \
    " SUMMARY =====")
    print("Total:", len(results))
    print("Selected:", len(selected))
    print("Rejected:", len(rejected))

