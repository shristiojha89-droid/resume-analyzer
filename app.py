
import pandas as pd
import streamlit as st
import PyPDF2



def predict_role(skills):
    if "machine learning" in skills and "python" in skills:
        return "🤖 Machine Learning Engineer"

    elif "html" in skills and "javascript" in skills:
        return "🌐 Web Developer"

    elif "python" in skills and "sql" in skills:
        return "📊 Data Analyst"

    elif "java" in skills:
        return "☕ Java Developer"

    else:
        return "🔍 General Software Role"


def calculate_score(skills):
    score = 0
    max_score = 0

    important_skills = ["python", "machine learning", "sql"]
    all_skills = ["python", "java", "html", "machine learning", "sql", "c++", "javascript"]

    for skill in all_skills:
        if skill in important_skills:
            max_score += 20
            if skill in skills:
                score += 20
        else:
            max_score += 10
            if skill in skills:
                score += 10

    return score, max_score



def give_suggestions(skills):
    suggestions = []

    if "python" not in skills:
        suggestions.append("Learn Python")

    if "machine learning" not in skills:
        suggestions.append("Add Machine Learning skills")

    if "sql" not in skills:
        suggestions.append("Learn SQL")

    return suggestions


def extract_skills(text):
    skills_list = ["python", "java", "html", "machine learning", "sql", "c++", "javascript"]
    
    found_skills = []
    text = text.lower()
    
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills

import re

def clean_words(s):
    return re.findall(r"\b[a-zA-Z]+\b", s.lower())

def match_score(resume_text, job_desc):
    r = set(clean_words(resume_text))
    j = set(clean_words(job_desc))

    if not j:
        return 0.0

    return round(len(r & j) / len(j) * 100, 2)

#AI feedback

def ai_feedback(skills, score):
    feedback = []

    if score < 40:
        feedback.append("Your resume is weak. Add more technical skills and projects.")

    elif score < 70:
        feedback.append("Your resume is average. Improve it by adding more relevant skills and experience.")

    else:
        feedback.append("Your resume looks strong. Focus on advanced skills and real-world projects.")

    if "machine learning" not in skills:
        feedback.append("Consider adding Machine Learning projects to stand out.")

    if "python" not in skills:
        feedback.append("Python is highly recommended for tech roles.")

    if len(skills) < 3:
        feedback.append("Add more skills to strengthen your profile.")

    return feedback

    

#upload resume

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume below 👇")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

job_desc = st.text_area("📋 Paste Job Description here")

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text

    return text

#Empty file check

# Empty file check
if uploaded_file is None:
    st.info("Please upload a PDF resume.")
    st.stop()

if uploaded_file:
    st.success("File uploaded successfully!")

# text extract
text = extract_text(uploaded_file)

# IMPORTANT CHECK
if not text.strip():
    st.error("⚠ Could not extract text from PDF.")
    st.stop()

# skills extraction
skills = sorted(list(set(extract_skills(text))))

if not skills:
    st.warning("⚠ No skills detected. Improve your resume!")


st.subheader("💡 Extracted Skills:")
st.write(skills)
st.subheader("📌 Total Skills Found:")
st.write(len(skills))

st.subheader("📄 Extracted Text (Preview):")
st.write(text[:500])

#score section

score, max_score = calculate_score(skills)
percentage = (score / max_score) * 100 if max_score != 0 else 0

st.subheader("📊 Resume Score:")
st.success(f"{score} / {max_score} ({round(percentage,2)}%)")
st.progress(min(int(percentage), 100))
st.caption(f"Score out of {max_score}")
    
#role prediction

role = predict_role(skills)
st.subheader("🎯 Predicted Job Role:")
st.success(role)

#Job Description

if job_desc.strip():
    match = match_score(text, job_desc)
    st.subheader("📊 Resume vs Job Match Score:")
    st.success(f"{match}% match")
else:
    st.warning("Paste a job description to get match score.")
    
#bar chart visualization

data = pd.DataFrame({
    "Skills": skills,
    "Count": [1]*len(skills)
})

st.subheader("📊 Skills Visualization:")
st.bar_chart(data.set_index("Skills"))


#suggestions

suggestions = give_suggestions(skills)
feedback = ai_feedback(skills, score)
st.subheader("📌 Suggestions:")
    
if not suggestions:
    st.success("✅ Your resume looks strong!")
else:
    for s in suggestions:
        st.markdown(f"👉 **{s}**")

import io
buf = io.StringIO()
buf.write("\n".join(suggestions) if suggestions else "Your resume looks strong!")
        
st.download_button(
    "📥 Download Suggestions",
    buf.getvalue(),
    "suggestions.txt"
)

st.subheader("🤖 AI Resume Feedback:")

for f in feedback:
    st.markdown(f"- {f}")




 

