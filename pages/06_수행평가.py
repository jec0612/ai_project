```python
# -----------------------------
# 추천 결과
# -----------------------------
st.subheader('✅ 추천 결과')

st.write(f'### 🌤 현재 계절: {season}')
st.write('## 🍹 추천 음료 리스트')

col1, col2 = st.columns(2)

for i, drink in enumerate(drinks):

    info = drink_info[drink]

    if i % 2 == 0:
        col = col1
    else:
        col = col2

    with col:

        with st.expander(f'🍹 {drink}'):

            st.markdown(
                f"""
                ### {drink}

                **🍴 맛**  
                {info['맛']}

                **✨ 효과**  
                {info['효과']}
                """
            )
```

