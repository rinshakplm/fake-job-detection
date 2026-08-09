import streamlit as st
st.set_page_config(page_title="Fake Job Posting Detector", layout="wide")
st.title(" Fake Job Posting Detection System")
st.subheader("Protecting job seekers using NLP and Machine Learning")
st.write("""
Welcome to our Fake Job Posting Detection app. This project uses 
Natural Language Processing (NLP), Machine Learning, Explainable AI (SHAP), 
and Generative AI (LLM) to identify potentially fraudulent job postings 
and explain the reasoning in plain, easy-to-understand language.

Use the sidebar to navigate to:
- **Dashboard** — explore data insights
- **Fake Job Detection** — check a job posting
- **Visualization** — see model performance and patterns
- **Prediction History** — view past checks
- **About** — learn more about this project
- **Contact/Help** — get support
""")
st.info("👈 Use the sidebar on the left to get started")