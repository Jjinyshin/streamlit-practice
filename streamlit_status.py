# streamlit_status.py

import streamlit as st

# Custom이 어렵다는 것이 단점이자 장점
# 수치 지표를 위한 st.metric
# 레이아웃을 잡아보자, 1줄이면 끝난다.

col1, col2, col3 = st.columns(3)

with col1:
  st.metric("풍속: ", "45km/h", "-4km/h")
with col2:
  st.metric("속도: ", "78%", "5km/h")
with col3:
  st.metric("온도: ", "28", "2")