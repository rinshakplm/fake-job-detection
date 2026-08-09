import streamlit as st

st.title("📩 Contact / Help")

st.write("""
### Need Help?

This tool is designed to help you quickly assess whether a job posting might be fraudulent. 
Here's how to use it effectively:

**How to use this app:**
1. Go to the **Fake Job Detection** page
2. Copy and paste the full job posting text (title, description, requirements, benefits)
3. Click "Check Job Posting" to get an instant prediction
4. Click "Why was this prediction made?" to see which words influenced the result
5. Check the **Prediction History** page to review past checks
6. Visit the **Dashboard** and **Visualization** pages for insights into fraud patterns

**Important Note**
This tool provides a probability-based assessment and is not 100% accurate. 
Always use your own judgment and verify job postings independently — 
research the company, avoid sharing personal/financial information upfront, 
and be cautious of postings requesting payment before employment.

**Red flags to watch for in job postings:**
- Requests for upfront payment or fees
- Urgent hiring with no interview process
- Unrealistic salary for minimal work
- Vague company details
- Communication only through personal email/WhatsApp

**Project Information**  
Built as a Data Science portfolio project using NLP, Machine Learning, and Explainable AI.
""")

st.divider()
st.info("For technical issues with this tool, please contact the project developer.")