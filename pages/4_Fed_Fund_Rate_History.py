from urllib.error import URLError

import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Fed Fund Rate History ", page_icon="📈")
st.markdown("# Fed Fund Rate History ")


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

file = "./data/Fed_Rate.csv"
df = load_data()

#url="https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv"
#df = pd.read_csv("https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv", sep=",")

st.line_chart(df, x= "Date", y= "Fed_Rate")

st.write("""Post GFC (Global Financial Crisis), first rate hike occurred in 2015 Dec; Fed Fund rate raised from 0.25 to 0.50%. After a total of 9 hikes of 25bps each, rate peaked at 2.5% in 2018 Dec. This hiking cycle (from trough to peak) lasted 3 years.  \n During the covid period, first cut occurred in 2019 Aug; Fed Fund rate cut from 2.5% to 2.25%. After a total rate cut of 2.25% consisting of 3 x 25bps, 1 x 50bps and 1 x 100bps, rate troughed at 0.25% in 2020 Mar. This cutting cycle (from peak to trough) lasted 7 months.  \n Against a global inflationary backdrop, first rate hike occurred in 2022 Mar, Fed Fund rate raised from 0.25 to 0.50%. After a total of 11 hikes consisting of 5 x 25bps, 2 x 50bps and 4 x 75bps, Fed Fund rate peaked at 5.5% in 2023 Jul. This hiking cycle (from trough to peak) lasted 1 year and 4 months.""")
