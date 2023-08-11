# streamlit_multimedia.py

import streamlit as st

# 탭으로 보여주기
tab1, tab2, tab3 = st.tabs(["이미지", "오디오", "비디오"])

with tab1:
  st.image("office_view.jpg")
with tab2:
  st.audio("demo.wav")
with tab3: 
  st.video("https://www.youtube.com/watch?v=Qb7yN9Rol2g")
  st.video("office_view.mp4")
