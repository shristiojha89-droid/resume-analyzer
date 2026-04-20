# AI Resume Analyzer

An AI-powered web application that analyzes resumes and provides structured insights including skill extraction, resume scoring, job role prediction, and intelligent feedback.

## Overview

AI Resume Analyzer is designed to help users evaluate and improve their resumes using automated analysis. The application processes PDF resumes, identifies key skills, calculates a performance score, and provides actionable suggestions along with AI-style feedback.

## Features

* Upload and analyze PDF resumes
* Automatic skill extraction
* Resume scoring with percentage
* Predicted job role based on skills
* Resume vs Job Description match score
* Skill visualization using charts
* Actionable improvement suggestions
* AI-based feedback for resume enhancement
* Downloadable suggestions file

## Tech Stack

* Python
* Streamlit
* Pandas
* PyPDF2

## Live Demo

https://ai-resume-analyzer-18042026.streamlit.app

## How It Works

1. Upload a resume in PDF format
2. The system extracts text and identifies relevant skills
3. A resume score is calculated based on predefined criteria
4. A suitable job role is predicted
5. Optional job description comparison generates a match score
6. Suggestions and AI feedback are provided for improvement

## Installation (Local Setup)

Clone the repository:

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```
resume-analyzer/
│── app.py
│── requirements.txt
│── README.md
```

## Future Improvements

* Integration with NLP-based skill extraction
* Advanced job matching using vector similarity
* Resume rewriting assistance
* Improved UI/UX design
* Support for multiple file formats

## Author

Developed as a project to demonstrate applied skills in Python, data processing, and web-based AI tools.

---

If you found this project useful, consider giving it a star.
