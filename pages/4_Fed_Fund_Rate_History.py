from urllib.error import URLError

import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Fed Fund Rate History ", page_icon="📈")
st.markdown("# Fed Fund Rate History ")
st.write("""The chart below shows the Fed Fund Rate History.""")

#url="https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv"
#df = pd.read_csv(url,index_col=0)
#df = pd.read_csv("https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv", sep=",")

#excel_file = 'Fed_Rate.xlsx'
#sheet_name = 'Sheet1'

#df = pd.read_excel(excel_file,
                   sheet_name=Sheet1,
                   usecols='A:B',
                   header=0)
df = pd.read_csv("Fed_Rate.csv")
st.line_chart(df)
