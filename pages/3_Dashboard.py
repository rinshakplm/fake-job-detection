import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Dashboard")
st.write("Exploratory insights from the job postings dataset")

@st.cache_data
def load_data():
    df = pd.read_csv('fake_job_postings.csv')
    return df

df = load_data()

# Basic stats
col1, col2, col3 = st.columns(3)
col1.metric("Total Postings", len(df))
col2.metric("Fake Postings", df['fraudulent'].sum())
col3.metric("Fake Rate", f"{(df['fraudulent'].sum()/len(df)*100):.1f}%")

st.divider()


st.subheader("Real vs Fake Job Postings")
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x='fraudulent', data=df, ax=ax)
ax.set_xlabel("Fraudulent (0 = Real, 1 = Fake)")
ax.set_ylabel("Count")
st.pyplot(fig)

st.divider()


st.subheader("Fake Posting Rate by Employment Type")
emp_fraud = df.groupby('employment_type')['fraudulent'].mean().sort_values(ascending=False) * 100
fig2, ax2 = plt.subplots(figsize=(8, 4))
emp_fraud.plot(kind='bar', ax=ax2, color='coral')
ax2.set_ylabel("Fake Rate (%)")
ax2.set_xlabel("Employment Type")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.divider()


st.subheader("Fake Posting Rate by Company Logo Presence")
logo_fraud = df.groupby('has_company_logo')['fraudulent'].mean() * 100
fig3, ax3 = plt.subplots(figsize=(6, 4))
logo_fraud.plot(kind='bar', ax=ax3, color=['green', 'red'])
ax3.set_xlabel("Has Company Logo (0 = No, 1 = Yes)")
ax3.set_ylabel("Fake Rate (%)")
plt.xticks(rotation=0)
st.pyplot(fig3)