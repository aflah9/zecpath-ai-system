from technical_ai.state_manager import create_session
from technical_ai.experience_logic import get_experience_level
from technical_ai.question_generator import generate_question
from technical_ai.scorer import evaluate_answer
from technical_ai.report_generator import generate_report


# =========================
# 1. CREATE CANDIDATE SESSION
# =========================
state = create_session(
    candidate_id="C1001",
    role="credit_analyst",   # you can change role here
    exp_level=get_experience_level(4)
)

print("\n🎯 Interview Started for:", state["candidate_id"])


# =========================
# 2. GENERATE QUESTION
# =========================
skill = "Financial_Analysis"
difficulty = "basic"

question = generate_question(skill, difficulty)

print("\n❓ Question Asked:")
print(question)

state["questions_asked"].append(question)


# =========================
# 3. SIMULATED ANSWER
# (later you will replace this with real user input)
# =========================
answer = "Credit analysis is used to evaluate borrower risk and repayment ability."

print("\n💬 Candidate Answer:")
print(answer)


# =========================
# 4. EVALUATE ANSWER
# =========================
score_label = evaluate_answer(answer,question)

# convert label → numeric score
if score_label == "good":
    score = 85
elif score_label == "average":
    score = 65
else:
    score = 40

state["scores"].append(score)

print("\n📊 Evaluation Result:", score_label, "->", score)


# =========================
# 5. GENERATE FINAL REPORT
# =========================
report = generate_report(state)

print("\n📄 FINAL REPORT")
print(report)