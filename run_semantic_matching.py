import json
from ai_engines.semantic_matcher import match_resume_to_jd

# Load Resume (your actual file)
with open("outputs/credit_analyst1_sambele_1b.pdf_final.json") as f:
    resume = json.load(f)

# Load JD (your parsed JD)
with open("outputs/jd_output.json") as f:
    jd = json.load(f)

# Run matching
result = match_resume_to_jd(resume, jd)
# 🔹 Save output
with open("outputs/semantic_results.json", "w") as f:
    json.dump(result, f, indent=4)

print("✅ RESULT:")
print(result)
print("✅ Saved to outputs/semantic_results.json")