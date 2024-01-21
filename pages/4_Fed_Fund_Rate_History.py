from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fed Fund Rate History ", page_icon="📈")
st.markdown("# Fed Fund Rate History ")
st.write("""The chart below shows the Fed Fund Rate History.""")

# url="https://github.com/hw-sg/treasury-assistant-streamlit-hw/blob/d5defa0c0ff536bd00026a04d3d2a0ce8290ae56/Fed_Rate.csv"
# source =pd.read_csv(url)


df = pd.read_csv("Fed_Rate.csv")
st.dataframe(df)

st.title("Fed Fund Rate History")

contact_options = ["Fed_Rate", "Date"]
contact_selected = st.selectbox("Select a Students value", contact_options)

inform = f"Students {contact_selected} Chart:"
fig = px.line(df, x="Name", y=contact_selected, title=inform)

st.plotly_chart(fig, use_container_width=True)
