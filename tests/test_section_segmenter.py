from parser.section_segmenter import segment_sections

def test_section_detection():

    sample_resume = """
    John Doe

    Skills
    Python, SQL, Machine Learning

    Work Experience
    Data Analyst at ABC Company

    Education
    BSc Computer Science
    """

    result = segment_sections(sample_resume)

    assert "skills" in result
    assert "experience" in result
    assert "education" in result