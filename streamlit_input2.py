# streamlit_input2.py

import streamlit as st

# picture = st.camera_input("사진찍기")

# if picture:
#   st.image(picture)

st.markdown("# 안녕하세요")
# 올해언젠가부터 가능해진 색상 조절, 5가지 색상만 가능
st.markdown("# :red[안녕하세요]")

# 과거의 방법
st.info("하윙")
st.error("하윙")
st.warning("하윙")
st.success("하윙")

import time

for i in range(5):
  # st.balloons()
  st.snow()
  time.sleep(3)

# streamlit이 제공하는 chart들이 있긴 한데.. 이렇게 이쁘지가 않음.
# 스트림릿 자체의 그래픽 기능은 약하지만, 다른 곳에서 가져온 것을 보여주는건 굿
# 예) matplotlib에서 생성한 그래프를 만들고 전달받아서 출력해줌!!