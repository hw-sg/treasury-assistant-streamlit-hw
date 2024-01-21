from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

import streamlit as st
import pandas as pd

from vega_datasets import data

st.set_page_config(page_title="Fed Fund Rate History ", page_icon="📈")
st.markdown("# Fed Fund Rate History ")
st.write("""The chart below shows the Fed Fund Rate History.""")

# assigning url to a variable
url="https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv"
 
# passing parameter to the function
source =pd.read_csv(url)

#source = data.stocks()

alt.Chart(source).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='Date',
    y='Fed_Rate'
)
