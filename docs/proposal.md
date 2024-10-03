# Resume Screening Application

**Prepared for**: UMBC Data Science Master's Capstone, supervised by Dr. Chaojie (Jay) Wang

**Author**: Supraja Bekkem

**GitHub Repository**: [https://github.com/SuprajaBekkem/UMBC-DATA606-Capstone.git]

**LinkedIn Profile**: [LinkedIn Profile]


**PowerPoint Presentation**: [PowerPoint Presentation Link]

**YouTube Video**: [YouTube Video Link]

---

## 1. Background

### Project Overview
The "Resume Screening Application" is designed to streamline the recruitment process by leveraging Natural Language Processing (NLP) techniques to automatically classify and rank resumes based on job requirements. The tool allows recruiters or hiring managers to upload resumes, and the app processes and ranks them based on how well they align with a given job description. This solution addresses one of the major challenges in recruitment—manually screening hundreds or thousands of resumes—which is both time-consuming and subject to human bias.

### Significance
Efficient and unbiased resume screening is critical to improving recruitment processes. By automating this step, recruiters can significantly reduce the time required to identify top candidates, improving the overall hiring experience. Additionally, it helps mitigate bias by focusing on skills, qualifications, and experience rather than irrelevant factors. This application serves to enhance both the accuracy and consistency of resume evaluations, leading to better-informed hiring decisions and a faster time-to-hire.

### Research Questions
- Can NLP models effectively classify and rank resumes based on their relevance to specific job descriptions?
- What combination of NLP techniques, such as word embeddings (TF-IDF, Word2Vec) and classification models (Logistic Regression, Random Forest), yields the best accuracy?
- How can unstructured resume data be preprocessed and structured to optimize model performance in ranking candidates?

---

## 2. Data

### Data Sources
The dataset was collected from Kaggle and is supplemented with additional sample resumes from various industries and job roles. Each resume consists of text data, containing both unstructured and semi-structured information, such as work experience, education, skills, and certifications.

### Data Table

| **Category**     | **Resume**                                                                                   |
|------------------|----------------------------------------------------------------------------------------------|
| Data Science     | Skills * Programming Languages: Python (pandas, numpy, scikit-learn, matplotlib), SQL, etc.   |
| Data Science     | Education Details: May 2013 to May 2017 B.E. in Computer Science from XYZ University.         |
| Data Science     | Areas of Interest: Deep Learning, Control Systems, Data Analytics, etc.                       |
| Data Science     | Skills: R, Python, SAP HANA, Tableau, Data Visualization.                                     |
| Data Science     | Education: MCA from YMCAUST, Faridabad; Project Experience in Data Mining.                    |

### Dataset Size
- Approximately 30 MB of data.
- Around 2,000 resumes.

### Data Structure
- **Number of resumes**: ~2,000.
- **Data Format**: Textual information extracted from resumes and job descriptions.
- **Columns**: Category(Majors), Resume.

### What Each Row Represents
Each row corresponds to an individual resume, and the columns contain various attributes such as skills, work experience, educational background, and additional metadata that are critical for matching against specific job requirements.

---
## 3. Exploratory Data Analysis (EDA)

In this section, we explore the dataset to gain insights into the distribution of resumes, word counts, and frequent terms. These insights help us understand the structure and characteristics of the data before model training.

### 3.1 Text Length Distribution

We analyze the distribution of word counts across resumes to understand the variation in resume lengths. This helps us identify whether resumes are typically short or long, and how this might affect model performance.

- **Observation**: The word count in resumes varies significantly, with some resumes being brief, while others are more detailed and lengthy.

### 3.2 Top Keywords

A word cloud was generated to identify the most frequently used words in the resumes. The common terms provide insight into what skills, qualifications, and experiences are most prevalent across all resumes.

- **Most Common Keywords**: Keywords such as "Python," "Machine Learning," "Data Science," "SQL," and "Java" are prevalent in the resumes, indicating that these are the core skills frequently mentioned in job applications related to the technical and data science fields.

### 3.3 Resume Category Distribution

We examined the distribution of resumes across various job categories. This analysis highlights whether there is any class imbalance that might impact model performance.

- **Observation**: The dataset contains an imbalance in job categories, with some categories such as "Data Science" and "Web Development" having a larger number of resumes compared to others.

### 3.4 Word Count by Job Category

We also calculated the average length of resumes for each job category to see if certain categories tend to have longer or shorter resumes.

- **Observation**: Resumes in categories like "Data Science" and "Software Engineering" tend to be longer, likely due to the technical skills and project descriptions that candidates include. In contrast, resumes in categories such as "HR" and "Testing" tend to be shorter.

### 3.5 Missing Data

We checked for missing data in the dataset to ensure there are no null values that could cause issues during model training.

- **Observation**: There are no missing values in the dataset, ensuring consistency for training machine learning models.

### 3.6 Class Imbalance

A closer look into class imbalance revealed that certain job categories have significantly more resumes compared to others. This imbalance may affect model performance, and we may need to apply techniques like oversampling or undersampling to balance the classes.

- **Observation**: Categories such as "Data Science" and "Web Development" are overrepresented compared to categories like "Mechanical Engineering" and "Civil Engineering."

---

## 4. Model Training

### NLP Techniques Utilized
- **Text Preprocessing**: The raw text is cleaned and preprocessed through tokenization, stopword removal, lemmatization, and normalization. This ensures that only relevant textual information is fed into the model.
- **Vectorization**: Textual data is converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) and Word2Vec embeddings, enabling the model to capture the semantic meaning of the resumes and job descriptions.
- **Classification Models**: Multiple machine learning models are employed for the classification and ranking of resumes:
  - **Logistic Regression**: A simple yet effective baseline model for classification tasks.
  - **Random Forest**: An ensemble model that improves accuracy by reducing variance.
  - **Gradient Boosting**: A more sophisticated model that iteratively corrects errors made by weaker models, resulting in higher accuracy and robustness.

### Performance Metrics
The models are evaluated based on key performance metrics such as:
- **Accuracy**: Measures the overall correctness of predictions.
- **Precision, Recall, and F1-Score**: Evaluates the model's ability to correctly classify resumes relevant to the job description, while minimizing false positives and false negatives.
- **ROC-AUC**: A metric that provides a balanced view of model performance across different classification thresholds, giving insight into the trade-offs between sensitivity and specificity.

---

## 5. Application of the Trained Models

The final model is deployed using **Streamlit**, a user-friendly platform for creating web applications. The application interface allows recruiters to upload resumes in bulk and input a job description for the system to analyze. The NLP model then processes the resumes, ranks them, and displays the best matches in descending order of relevance. This intuitive interface enables quick access to the most qualified candidates, significantly enhancing the speed and efficacy of the recruitment process.

---

## 6. Conclusion

This capstone project demonstrates how NLP and machine learning can effectively automate and improve the process of resume screening. By reducing manual effort, minimizing biases, and providing a scalable solution, this application offers substantial value to hiring teams across industries. Future work will focus on:
- Refining the ranking criteria to consider additional factors such as soft skills and cultural fit.
- Expanding the dataset to include a more diverse range of resumes across different job sectors.
- Incorporating additional features such as skill-level matching, real-time collaboration between recruiters, and applicant tracking system (ATS) integration.

---

## Key Features and Future Enhancements

To make the app stand out further, some key features and future enhancements could include:
- **Skill extraction**: Advanced techniques to extract and match specific skills between resumes and job descriptions.
- **Bias mitigation**: Algorithms to anonymize personal data (name, gender, etc.) to reduce unconscious bias.
- **Candidate recommendations**: Suggest alternative job roles for candidates who may be more suitable for different roles within the organization.
- **Real-time feedback and collaboration**: Allow recruiters to interact and collaborate within the app to refine the resume ranking process.


By continuously enhancing the features and scalability of this application, the platform has the potential to become a go-to tool for organizations seeking efficient and unbiased resume screening solutions.

