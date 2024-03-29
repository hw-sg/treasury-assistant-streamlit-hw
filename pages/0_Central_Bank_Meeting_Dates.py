from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code


import streamlit as st
import pandas as pd

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df

st.set_page_config(page_title="Central Bank Meeting Dates", page_icon="📈")
st.markdown("# Central Bank Meeting Dates ")
st.write("""The below table list down the various Central Banks' meetings date in 2024. Select "Add filters" to filter by different country.""")

df = pd.DataFrame(
    [
        {"Month": "Jan", "Quarter": 1, "Country": "US", "Date": "2024/01/31",},
        {"Month": "Feb", "Quarter": 1, "Country": "AU", "Date": "2024/02/06",},
        {"Month": "Mar", "Quarter": 1, "Country": "US", "Date": "2024/03/20",},
        {"Month": "Mar", "Quarter": 1, "Country": "AU", "Date": "2024/03/19",},
        {"Month": "May", "Quarter": 2, "Country": "US", "Date": "2024/05/01",},
        {"Month": "May", "Quarter": 2, "Country": "AU", "Date": "2024/05/07",},
        {"Month": "Jun", "Quarter": 2, "Country": "US", "Date": "2024/06/12",},
        {"Month": "Jun", "Quarter": 2, "Country": "AU", "Date": "2024/06/18",},
        {"Month": "Jul", "Quarter": 3, "Country": "US", "Date": "2024/07/31",},
        {"Month": "Aug", "Quarter": 3, "Country": "US", "Date": "2024/08/20",},
        {"Month": "Aug", "Quarter": 3, "Country": "AU", "Date": "2024/08/06",},
        {"Month": "Sep", "Quarter": 3, "Country": "AU", "Date": "2024/09/24",},
        {"Month": "Nov", "Quarter": 4, "Country": "AU", "Date": "2024/11/05",},
        {"Month": "Nov", "Quarter": 4, "Country": "US", "Date": "2024/11/07",},
        {"Month": "Dec", "Quarter": 4, "Country": "AU", "Date": "2024/12/10",},
        {"Month": "Dec", "Quarter": 4, "Country": "US", "Date": "2024/12/18",},
    ]
)

#st.dataframe(df, use_container_width=True)

st.dataframe(filter_dataframe(df))
