# streamlit_app.py
import streamlit as st

from app import get_video_details

st.title("📺 YouTube Viewing Pattern Analyzer")

query = st.text_input("Search Topic", "Netflix Trailer")
if st.button("Fetch Data"):
    data = get_video_details(query)  # noqa: F821
    st.dataframe(data.head())
    st.bar_chart(data.sort_values(by='Views', ascending=False)
                 .set_index('Video Title')['Views'].head(10))