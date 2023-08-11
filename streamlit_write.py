# streamlit_write.py

# 스트림릿은 마크다운을 기본으로 한다.
# 핫 리로드 기능도 지원한다!
import streamlit as st

st.title("제목이야")
st.markdown("# 제목")

st.header("header")
st.markdown("## :blush: header")

st.subheader("subheader")
st.text("text")

# 수식 넣기
st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")
# python의 print와 똑같은 write
st.write(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")