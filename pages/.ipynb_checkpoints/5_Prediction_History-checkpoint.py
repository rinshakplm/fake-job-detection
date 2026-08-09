import streamlit as st
import pandas as pd
import os

st.title(" Prediction History")
st.write("View past job postings checked using this tool")

HISTORY_FILE = "prediction_history.csv"

if os.path.exists(HISTORY_FILE):
    history_df = pd.read_csv(HISTORY_FILE)
    if len(history_df) > 0:
        st.dataframe(history_df.sort_index(ascending=False), use_container_width=True)
        
        if st.button("Clear History"):
            os.remove(HISTORY_FILE)
            st.success("History cleared!")
            st.rerun()
    else:
        st.info("No predictions made yet. Go to 'Fake Job Detection' to check a posting.")
else:
    st.info("No predictions made yet. Go to 'Fake Job Detection' to check a posting.")