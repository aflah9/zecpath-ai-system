import re
import spacy


nlp = spacy.load("en_core_web_md")



SECTION_HEADERS = {
    "skills": [
        "skills", "technical skills", "key skills",
        "core skills", "key competencies",
        "technical competencies", "tools", "tools technologies"
    ],
    "experience": [
        "experience", "work experience",
        "professional experience", "employment history"
    ],
    "education": [
        "education", "academic background",
        "academic qualifications"
    ],
    "summary": [
        "summary", "professional summary",
        "profile", "profile summary"
    ]
}


SECTION_LABELS = {
    "skills": "skills",
    "experience": "work experience",
    "education": "education",
    "summary": "professional summary"
}


def segment_sections(text):


    # 🔥 Add line breaks before headings
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


        # ✅ Rule-based
        for section, keywords in SECTION_HEADERS.items():
            if any(keyword.lower() in clean_line for keyword in keywords) and len(clean_line.split()) <= 5:
                found_section = section
                break


        # ✅ NLP fallback (SAFE VERSION)
        # 
        if not found_section and len(clean_line.split()) <= 5:

            if clean_line.strip():  # 🔥 avoid empty lines
                doc1 = nlp(clean_line)

                if doc1.vector_norm > 0:  # 🔥 ensure valid vector

                    for section, label in SECTION_LABELS.items():
                        doc2 = nlp(label)

                        if doc2.vector_norm > 0:  # 🔥 ensure valid vector

                            if doc1.similarity(doc2) > 0.7:
                                found_section = section
                                break


        if found_section:
            current_section = found_section
            if current_section not in sections:
                sections[current_section] = ""
        else:
            sections[current_section] += line + "\n"


    return sections


