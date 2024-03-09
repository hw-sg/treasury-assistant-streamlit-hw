import numpy as np

import streamlit as st


st.set_page_config(page_title="Trading Signal ", page_icon="📹")
st.markdown("# Trading Signal ")
st.sidebar.header("Trading Signal ")
st.write(
    """Strong trading signal arises when a FED official changes his stance from dovish to hawkish or vice versa."""
)
st.image('sentiment2.jpg', caption='Sentiment analysis of a FED voting member')
