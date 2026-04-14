import os
from ai_engines.resume_text_extractor import ResumeTextExtractor

def test_resume_extractor():
    extractor = ResumeTextExtractor()

    folder_path = "sample_resumes"

    assert os.path.exists(folder_path), "sample_resumes folder not found"

    for file in os.listdir(folder_path):
        if file.endswith(".pdf") or file.endswith(".docx"):
            file_path = os.path.join(folder_path, file)

            text = extractor.extract_text(file_path)

            # ✅ basic checks
            assert isinstance(text, str)
            assert len(text) > 0
            
    