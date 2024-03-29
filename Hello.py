# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Treasury Assistant! ")

    st.sidebar.success("Select an option above.")

    st.write("""This app leverages LLM (Large Language Model) technique to perform sentiment analysis on FED speeches with the objective of deriving trading signals.  \n\n The app also has other useful functions such as showing the historical movement of Fed Fund Rates and Central Bank Meeting dates, so as to provide users with more insights and convenience in a one-stop app.""")


if __name__ == "__main__":
    run()
