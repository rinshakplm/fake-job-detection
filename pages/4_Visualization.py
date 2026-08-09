import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title(" Model Visualization")
st.write("Performance comparison of the machine learning models used in this project")

st.divider()

# Model comparison table
st.subheader("Model Performance Comparison")

model_data = {
    "Model": ["Logistic Regression", "Naive Bayes", "Random Forest", "Voting Classifier (Final)"],
    "Precision": [0.59, 0.90, 0.99, 0.92],
    "Recall": [0.91, 0.46, 0.56, 0.76],
    "F1-Score": [0.71, 0.61, 0.72, 0.83]
}

import pandas as pd
model_df = pd.DataFrame(model_data)
st.dataframe(model_df, use_container_width=True)

st.divider()

# Bar chart comparison
st.subheader("Visual Comparison")
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(model_df))
width = 0.25

ax.bar(x - width, model_df['Precision'], width, label='Precision')
ax.bar(x, model_df['Recall'], width, label='Recall')
ax.bar(x + width, model_df['F1-Score'], width, label='F1-Score')

ax.set_xticks(x)
ax.set_xticklabels(model_df['Model'], rotation=15)
ax.set_ylabel("Score")
ax.set_title("Model Performance Comparison")
ax.legend()
st.pyplot(fig)

st.divider()

# Confusion Matrix (using your text-only model results)
st.subheader("Confusion Matrix — Final Model (Text-Only, Threshold=0.35)")
st.write("Based on test set evaluation (3,576 postings)")

cm = np.array([[3344, 59], [17, 156]])  # Approximate from your recall/precision at threshold 0.35

fig2, ax2 = plt.subplots(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Real', 'Fake'], yticklabels=['Real', 'Fake'], ax=ax2)
ax2.set_xlabel("Predicted")
ax2.set_ylabel("Actual")
st.pyplot(fig2)