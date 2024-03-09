
import numpy as np

import streamlit as st


st.set_page_config(page_title="FED Speech Sentiment", page_icon="📹")
st.markdown("# FED Speech Sentiment")
st.sidebar.header("FED Speech Sentiment")
st.write(
    """This app shows the results of using LLM to perform sentiment analysis on FED speeches to derive trading signals."""
)
st.image('sentiment.jpg', caption='Sentiment analysis of FOMC speech')

