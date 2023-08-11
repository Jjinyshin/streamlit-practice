# streamlit_data.py

import streamlit as st
import pandas as pd

df = pd.read_csv("titanic.csv")
st.write(df)
st.dataframe(df)

with st.expander("한번에 전체보기"):
  st.table(df)