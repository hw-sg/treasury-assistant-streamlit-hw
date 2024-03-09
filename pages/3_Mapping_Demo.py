import numpy as np

import streamlit as st


st.set_page_config(page_title="Trading Signal ", page_icon="📹")
st.markdown("# Trading Signal ")
st.sidebar.header("Trading Signal ")
st.write(
    """Strong trading signal arises when a FED official changes his stance from dovish to hawkish or vice versa. /n/n In the below highlighted instance, the change from dovish (-0.8) to hawkish (0.4) signals that interest rate is going to increase, which can be a trading signal to sell bonds or borrow funds"""
)
st.image('sentiment2.jpg', caption='Sentiment analysis of a FED voting member')
