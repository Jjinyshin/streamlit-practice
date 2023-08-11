# streamlit_input.py

import streamlit as st

result_button = st.button("눌러줘")
st.write(result_button)

result_checkbox = st.checkbox("동의")
st.write(result_checkbox)

result_radio = st.radio(
  "어떤 사이트를 사용하실 예정이신가요?", ["Youtube", "Naver"], 
  0
  )
st.write(result_radio)

result_selectbox = st.selectbox(
  "어떤 사이트를 사용하실 예정이신가요?", ["Youtube", "Naver"], 
  0
)
st.write(result_selectbox)

result_multibox = st.multiselect(
  "어떤 사이트를 사용하실 예정이신가요?", ["Youtube", "Naver news", "Naver map"], 
)
st.write(result_multibox)

result_slider = st.slider("숫자 선택",
0, 101, value=50, step=2
)
st.write(result_slider)

result_number = st.number_input(
  "나이 입력",
  min_value=18, max_value=60, step=2
)
st.write(result_number)
# max_value 이상의 값을 입력하면 "값은 60 이하여야 합니다." 라는 validation처리까지 해준다ㄷㄷ


import datetime
result_date = st.date_input("며칠에 출발?", datetime.date(2023,12,1))
st.write(result_date)

result_time = st.time_input("몇시에 출발?", datetime.time(12,12,1))
st.write(result_time)