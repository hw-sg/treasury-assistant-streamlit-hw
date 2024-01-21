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

source = data.stocks()

alt.Chart(source).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='date',
    y='price'
).transform_filter(alt.datum.symbol == 'GOOG')
