
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

def match_score(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    match_count = 0

    for word in job_desc.split():
        if word in resume_text:
            match_count += 1

    score = (match_count / len(job_desc.split())) * 100
    return round(score, 2)

#upload resume

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume below 👇")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

job_desc = st.text_area("📋 Paste Job Description here")

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    text = extract_text(uploaded_file)
    skills = extract_skills(text)

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
    st.progress(int(percentage))


    role = predict_role(skills)
    st.subheader("🎯 Predicted Job Role:")
    st.success(role)

    if job_desc:
        match = match_score(text, job_desc)
        st.subheader("📊 Resume vs Job Match Score:")
        st.success(f"{match}% match")
    
    #bar chart visualization

    data = pd.DataFrame({
        "Skills": skills,
        "Count": [1]*len(skills)
    })

    
    st.subheader("📊 Skills Visualization:")
    st.bar_chart(data.set_index("Skills"))

    suggestions = give_suggestions(skills)
    st.subheader("📌 Suggestions:")

    if not suggestions:
        st.success("✅ Your resume looks strong!")
    else:
        for s in suggestions:
            st.markdown(f"👉 **{s}**")
 

