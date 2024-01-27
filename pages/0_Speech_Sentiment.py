
import numpy as np

import streamlit as st


st.set_page_config(page_title="Speech Sentiment", page_icon="📹")
st.markdown("# Speech Sentiment")
st.sidebar.header("Speech Sentiment")
st.write(
    """This app shows the results of using Gen AI to perform sentiment analysis on FOMC speech to derive trading signals."""
)
st.image('sentiment.jpg', caption='Sentiment analysis of FOMC speech')

