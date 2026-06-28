from interview_ai.final_hr_module import run_hr_interview


def run_live_demo():

    result = run_hr_interview(
        candidate_id="C1001",

        answers=[
            {
                "question_id": "Q1",
                "relevance_score": 0.90,
                "communication_score": 82,
                "confidence_score": 78,
                "contradiction": False,
                "is_vague": False
            },
            {
                "question_id": "Q2",
                "relevance_score": 0.85,
                "communication_score": 80,
                "confidence_score": 77,
                "contradiction": False,
                "is_vague": False
            }
        ],

        communication={
            "communication_score": 82
        },

        behavior={
            "confidence": {
                "confidence_score": 78
            },
            "behavioral_score": 80,
            "contradiction": False
        }
    )

    # ----------------------------
    # LIVE DEMO FORMAT OUTPUT
    # ----------------------------

    live_output = {
        "candidate_id": result["candidate_id"],
        "scores": {
            "communication": result["scores"]["communication"],
            "confidence": result["scores"]["confidence"],
            "aptitude": 80,   # simulated (you don’t yet have aptitude engine wired here)
            "hr": result["scores"]["hr"]
        },
        "final_score": result["final_score"],
        "decision": "Hire" if result["final_score"] >= 75 else "Consider"
    }

    print("\n================ LIVE DEMO OUTPUT ================\n")
    print(live_output)

    print("\nEXPLANATION:\n")

    print("Communication:", live_output["scores"]["communication"], "/100")
    print("Candidate communicates clearly.\n")

    print("Confidence:", live_output["scores"]["confidence"], "/100")
    print("Some hesitation but generally confident.\n")

    print("Aptitude:", live_output["scores"]["aptitude"], "/100")
    print("Good logical reasoning.\n")

    print("HR:", live_output["scores"]["hr"], "/100")
    print("Relevant and structured answers.\n")


if __name__ == "__main__":
    run_live_demo()



from ai_core.aggregation_pipeline import aggregation_pipeline

print("\n================ DAY 51 DEMO ================\n")

result = aggregation_pipeline(
    candidate_id="C9001",
    scores={
        "ats": 75,
        "screening": 70,
        "hr": 80,
        "technical": 85,
        "machine_test": 78
    },
    role_type="technical"
)

print(result)