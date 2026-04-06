import os
import pdfplumber
from docx import Document
from utils.text_cleaner import clean_text

class ResumeTextExtractor:

    def extract_text(self, file_path):
        ext = file_path.split('.')[-1].lower()

        if ext == 'pdf':
            raw_text = self._read_pdf(file_path)
        elif ext == 'docx':
            raw_text = self._read_docx(file_path)
        else:
            raise ValueError("Unsupported file format")

        cleaned_text = clean_text(raw_text)
        return cleaned_text

    def _read_pdf(self, file_path):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    def _read_docx(self, file_path):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    