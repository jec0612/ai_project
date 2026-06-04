import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------
# 클릭 가능한 추천 음료 박스
# -----------------------------
st.subheader('✅ 추천 결과')

st.markdown(f'''
<div style="
    background-color:#f5f5f5;
    padding:25px;
    border-radius:20px;
    border:2px solid #dcdcdc;
    text-align:center;
">
    <h2>🌤 현재 계절: {season}</h2>
    <h3>🍹 추천 음료 리스트 🍹</h3>
</div>
''', unsafe_allow_html=True)

st.write('')

col1, col2 = st.columns(2)

for i, drink in enumerate(drinks):

    info = drink_info[drink]

    if i % 2 == 0:
        current_col = col1
    else:
        current_col = col2

    with current_col:

        with st.expander(f'{drink} 클릭하기'):

            st.markdown(f'''
            <div style="
                background-color:#ffffff;
                padding:20px;
                border-radius:15px;
                border:2px solid #dddddd;
                margin-bottom:10px;
            ">
                <h3>{drink}</h3>

                <p>
                <b>🍴 맛</b><br>
                {info['맛']}
                </p>

                <p>
                <b>✨ 효과</b><br>
                {info['효과']}
                </p>

            </div>
            ''', unsafe_allow_html=True)
```
