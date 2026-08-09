import streamlit as st
import pickle
import re
import pandas as pd
import os
from datetime import datetime
import shap
from groq import Groq

st.title(" Fake Job Posting Detection")
st.write("Paste the full job posting below (copy-paste directly from the job site or email).")

@st.cache_resource
def load_files():
    with open('voting_model_text.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    return model, tfidf

model, tfidf = load_files()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

job_posting = st.text_area("Paste the job posting here", height=300,
                             placeholder="Paste the full job title, description, requirements, and benefits here...")

if st.button("Check Job Posting"):
    if job_posting.strip() == "":
        st.warning("Please paste a job posting first.")
    else:
        cleaned = clean_text(job_posting)
        X_text_input = tfidf.transform([cleaned])

        probability = model.predict_proba(X_text_input)[0][1]
        prediction = 1 if probability >= 0.35 else 0

        st.divider()
        if prediction == 1:
            st.error(f" This posting is likely FAKE ({probability*100:.1f}% confidence)")
        else:
            st.success(f"This posting is likely REAL ({(1-probability)*100:.1f}% confidence)")

        # Save to history
        HISTORY_FILE = "prediction_history.csv"
        new_entry = pd.DataFrame([{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "job_snippet": job_posting[:100] + "..." if len(job_posting) > 100 else job_posting,
            "prediction": "FAKE" if prediction == 1 else "REAL",
            "confidence": f"{probability*100:.1f}%" if prediction == 1 else f"{(1-probability)*100:.1f}%"
        }])
        if os.path.exists(HISTORY_FILE):
            new_entry.to_csv(HISTORY_FILE, mode='a', header=False, index=False)
        else:
            new_entry.to_csv(HISTORY_FILE, index=False)

        # Explainable AI - ONLY shown when prediction is FAKE
        if prediction == 1:
            st.divider()
            with st.expander("Why was this prediction made? (Explainable AI)"):
                with st.spinner("Analyzing key words..."):
                    rf_model = model.named_estimators_['rf']
                    explainer = shap.TreeExplainer(rf_model)

                    X_dense = X_text_input.toarray().astype(float)
                    shap_values = explainer.shap_values(X_dense, check_additivity=False)
                    shap_values_fake = shap_values[:, :, 1][0]

                    feature_names = tfidf.get_feature_names_out()

                    present_word_indices = X_dense[0].nonzero()[0]
                    word_impact = [(feature_names[i], shap_values_fake[i]) for i in present_word_indices]

                    fake_words = [(word, impact) for word, impact in word_impact if impact > 0]
                    fake_words_sorted = sorted(fake_words, key=lambda x: x[1], reverse=True)
                    top_fake_words = fake_words_sorted[:10]

                    if len(top_fake_words) == 0:
                        st.write("No strong fake-indicating words detected in this posting.")
                    else:
                        st.write("**Words in this posting that raised fraud suspicion:**")
                        for word, impact in top_fake_words:
                            st.write(f"🔴 **{word}**")

                        # LLM-generated natural language explanation
                        st.divider()
                        st.write("**AI Summary:**")
                        with st.spinner("Generating explanation..."):
                            groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"]) 

                            words_list = [word for word, impact in top_fake_words]
                            words_str = ", ".join(words_list)

                            prompt = f"""A machine learning model analyzed a job posting and predicted it is FAKE with {probability*100:.1f}% confidence.
The following suspicious words/phrases were found: {words_str}.

Write a brief, clear, 2-3 sentence explanation for a non-technical job seeker about why this posting might be risky. Be direct and practical."""

                            llm_response = groq_client.chat.completions.create(
                                model="llama-3.1-8b-instant",
                                messages=[{"role": "user", "content": prompt}]
                            )
                            st.write(llm_response.choices[0].message.content)