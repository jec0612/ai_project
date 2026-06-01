```python
# -----------------------------
# 클릭형 추천 음료 카드
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

    card_html = f'''
    <div style="
        background-color:white;
        padding:18px;
        border-radius:18px;
        border:2px solid #e0e0e0;
        margin-bottom:15px;
        box-shadow:2px 2px 10px rgba(0,0,0,0.1);
    ">
        <h3 style="text-align:center;">{drink}</h3>
        <hr>
        <p><b>🍴 맛</b><br>{info['맛']}</p>
        <p><b>✨ 효과</b><br>{info['효과']}</p>
    </div>
    '''

    if i % 2 == 0:
        with col1:
            with st.expander(f'👉 {drink}'):
                st.markdown(card_html, unsafe_allow_html=True)
    else:
        with col2:
            with st.expander(f'👉 {drink}'):
                st.markdown(card_html, unsafe_allow_html=True)
```
