import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import docx

# Define the resume cleaning function
def clean_resume_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabetic characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

# Function to extract text from a DOCX file
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return '\n'.join([para.text for para in doc.paragraphs])

# Load the TfidfVectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

# Load the trained classifier model 
with open('logistic_regression_model.pkl', 'rb') as f: 
    clf = pickle.load(f)

# Define the mapping of category IDs to category names
category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}

# Streamlit app
def main():
    st.title("Resume Categorization and Job Matching App")

    st.write("""
    This app classifies resumes into different job categories and calculates the similarity between resumes and a given job description.
    """)

    # Step 1: Add job description input
    job_description = st.text_area("Enter the job description", height=200)

    # Upload multiple resume files
    uploaded_files = st.file_uploader("Upload your resumes (txt, pdf, docx)", type=["txt", "pdf", "docx"], accept_multiple_files=True)

    if uploaded_files and job_description:
        results = []
        cleaned_job_description = clean_resume_text(job_description)

        # Transform the job description using the TfidfVectorizer
        job_description_vector = tfidf_vectorizer.transform([cleaned_job_description])

        for uploaded_file in uploaded_files:
            file_type = uploaded_file.name.split('.')[-1].lower()

            # Step 2: Extract text based on file type
            if file_type == "txt":
                resume_text = uploaded_file.read().decode("utf-8")
            elif file_type == "pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            elif file_type == "docx":
                resume_text = extract_text_from_docx(uploaded_file)
            else:
                st.error(f"Unsupported file format: {file_type}")
                continue

            # Step 3: Clean the extracted text
            cleaned_resume = clean_resume_text(resume_text)

            # Step 4: Transform the cleaned resume using the loaded TfidfVectorizer
            resume_vector = tfidf_vectorizer.transform([cleaned_resume])

            # Step 5: Make the prediction using the loaded classifier (for categorization)
            prediction_id = clf.predict(resume_vector)[0]

            # Step 6: Map the predicted category ID to the corresponding category name
            category_name = category_mapping.get(prediction_id, "Unknown")

            # Step 7: Calculate cosine similarity between the job description and the resume
            similarity_score = cosine_similarity(job_description_vector, resume_vector)[0][0] * 100  # Convert to percentage

            # Step 8: Append the result for display later
            results.append(f"**{uploaded_file.name}** classified as: **{category_name}** | Similarity Score: **{similarity_score:.2f}%**")

        # Step 9: Display the classification results along with the similarity score
        st.write("\n".join(results))

if __name__ == "__main__":
    main()
