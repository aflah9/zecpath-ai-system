import os
from parser.section_segmenter import segment_sections
from ai_engines.resume_text_extractor import ResumeTextExtractor  # your PDF reader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLES_FOLDER = os.path.join(BASE_DIR, "sample_resumes")


extractor = ResumeTextExtractor() 

for file in os.listdir(SAMPLES_FOLDER):

    if file.endswith(".pdf"):
        path = os.path.join(SAMPLES_FOLDER, file)

        print("\n============================")
        print("Processing:", file)
        print("============================")

        # 🔥 Use PDF extractor inste
        # ad of open()
        extractor = ResumeTextExtractor()
        text = extractor.extract_text(path)

        print("\nRAW TEXT:\n", text[:500])

        sections = segment_sections(text)

        for section, content in sections.items():
            print("\nSECTION:", section.upper())
            print(content)