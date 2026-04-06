import re
#import spacy

#nlp = spacy.load("en_core_web_sm")

SECTION_HEADERS = {
    "skills": [
        "skills",
        "Skills",
        "technical skills",
        "key skills",
        "core skills",
        "Key Competencies",
        "key competencies",
        "technical competencies",
        "Technical Skills",
        "Core Skills",
        "Tools Technologies",
         "tools", "tools technologies"

    ],

    "experience": [
        "experience",
        "Experience",
        "Work Experience",
        "professional experience",
        "employment history",
        "Professional Experience",
        "work experience"
    ],

    "education": [
        "education",
        "Education",
        "academic background",
        "academic qualifications",
        "Academic Background"
    ],

    "summary": [
        "summary",
        "Profile Summary"
        "professional summary",
        "profile",
        "profile summary",
        "Professional Summary"
    ]
}


SECTION_HEADERS = {
    "skills": ["skills"],
    "experience": ["experience"],
    "education": ["education"],
    "summary": ["summary", "professional summary", "profile"]
}

def segment_sections(text):

    # 🔥 Step 1: Add line breaks ONLY for likely headings (ALL CAPS or short words)
    text = re.sub(
    r'\b(SKILLS|EXPERIENCE|EDUCATION|PROFESSIONAL SUMMARY|PROFILE SUMMARY|SUMMARY|PROFILE|WORK EXPERIENCE|KEY SKILLS|CORE SKILLS|TECHNICAL SKILLS|KEY COMPETENCIES|TOOLS|TOOLS TECHNOLOGIES|ACADEMIC BACKGROUND)\b',
    lambda x: "\n" + x.group(0) + "\n",
    text
    )

    sections = {}
    current_section = "other"
    sections[current_section] = ""

    lines = text.split("\n")

    for line in lines:
        clean_line = re.sub(r'[^a-zA-Z ]', '', line).lower().strip()

        found_section = None

        for section, keywords in SECTION_HEADERS.items():
            if any(keyword in clean_line for keyword in keywords) and len(clean_line.split()) <= 5:
                found_section = section
                break

        if found_section:
            current_section = found_section
            if current_section not in sections:
                sections[current_section] = ""
        else:
            sections[current_section] += line + "\n"

    return sections