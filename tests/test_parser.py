from parser.resume_parser import ResumeParser

def test_resume_parser():
    parser = ResumeParser()
    result = parser.parse("Sample Resume")
    assert isinstance(result, dict)
    

