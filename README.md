

 #  PROJECT OVER VIEW

 Zecpath AI System is a modular AI recruitment
 pipeline 
designed for resume parsing, ATS scoring, candidate screening, 
and interview preparation.
An end-to-end AI-powered recruitment system developed during my AI Developer internship at Zecsar Business LLP to assist with resume processing, ATS-oriented evaluation, candidate screening, interview assessment, scoring, and recruitment decision support.

# PROJEXT STRUCTURE

Project Structure:

data/              - Dataset storage
parsers/           - Resume parsing logic
ats_engine/        - ATS scoring engine
screening_ai/      - Screening logic
interview_ai/      - Interview module
scoring/           - Candidate scoring
utils/             - Utility functions (logging)
tests/             - Unit tests
main.py            - Entry point
requirements.txt   - Dependencies

## Setup Instructions

1. Clone repository
2. Create virtual environment:
   python -m venv venv

3. Activate environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt
   

## Key Features

* Resume upload and processing
* NLP-based resume information extraction
* Candidate skill and keyword identification
* ATS-oriented resume evaluation
* Candidate screening
* Interview evaluation
* Candidate scoring
* Decision-support workflow
* RESTful API integration
* Input validation and exception handling
* Logging and error management
* Automated API testing
* End-to-end workflow validation

## End-to-End Workflow

```text
Resume
   ↓
Resume Processing
   ↓
NLP Extraction
   ↓
ATS Evaluation
   ↓
Candidate Screening
   ↓
Interview Evaluation
   ↓
Candidate Scoring
   ↓
Final Decision Support
```

## Technology Stack

* Python
* FastAPI
* spaCy
* NLP
* Scikit-learn
* Pandas
* NumPy
* REST APIs
* Git/GitHub

## System Architecture

The application uses a modular backend architecture where FastAPI provides the API layer, NLP components process resume content, and evaluation modules generate structured candidate scores and recruitment insights.

## API Layer

FastAPI is used to expose the system functionality through RESTful endpoints.

Major operations include:

* Resume upload
* Resume processing
* Candidate analysis
* ATS evaluation
* Screening
* Interview evaluation
* Candidate scoring

## Testing

The system was tested across individual modules and the complete recruitment workflow.

Testing covered:

* API endpoint validation
* File upload handling
* Resume processing
* NLP processing
* Input validation
* Exception handling
* Candidate scoring
* End-to-end workflow integration

## Development Challenges

During development, issues were identified in areas such as API integration, file processing, NLP processing, validation, and module integration.

These issues were investigated through debugging and testing, followed by iterative fixes and validation.

## Project Outcome

The completed system demonstrates the integration of **AI/NLP processing with backend API development** to create a practical recruitment automation workflow.

## My Contribution

As an AI Developer Intern, I worked on:

* AI/NLP implementation
* Resume processing
* Candidate evaluation logic
* API development
* Integration
* Testing and debugging
* Documentation
* Final demo and knowledge transfer

## Future Improvements

Potential improvements include:

* Advanced semantic resume-to-job matching
* Transformer/LLM-based candidate analysis
* Vector database integration
* Explainable candidate scoring
* Authentication and role-based access
* Production database integration
* Docker-based deployment
* Monitoring and analytics dashboard
* Automated model evaluation and performance tracking

```
```



   