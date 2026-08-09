import streamlit as st

st.title(" About This Project")

st.write("""
### Fake Job Posting Detection System

This project uses Natural Language Processing (NLP), Machine Learning,  
Explainable AI (SHAP) and LLM to identify potentially fraudulent job postings, helping 
protect job seekers from scams.

**Problem Statement**  
Fake job postings are a growing concern, often used to collect personal information, 
request upfront payments, or commit fraud. This tool analyzes job posting text 
to flag suspicious listings.

**Dataset**  
"Real or Fake Job Posting Prediction" dataset from Kaggle, containing ~17,880 
job postings.

**Tech Stack**
- Python, pandas, numpy
- NLP: NLTK, TF-IDF (scikit-learn)
- Machine Learning: Logistic Regression, Random Forest, Voting Classifier (ensemble)
- SQL: SQLite for data insights
- Explainable AI: SHAP
- Genrative AI: Groq API (Llama 3.1) for natural language explanations
- Web App: Streamlit


**Model Performance**  
Our final ensemble model (Voting Classifier) achieves 92% precision and 76% recall 
at default threshold, improved to 90% recall at an optimized threshold of 0.35 — 
prioritizing catching fraudulent postings.

**Approach**
1. Data cleaning and exploratory data analysis
2. SQL-based insights on posting patterns
3. NLP preprocessing and TF-IDF vectorization
4. Training and comparing multiple ML models
5. Building an ensemble model for best performance
6. SHAP-based explainability
7. Deploying as an interactive Streamlit application
""")