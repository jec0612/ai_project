import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 읽기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 컬럼 공백 제거
df.columns = df.columns.str.strip()

# 날짜 문자열 정리
df['날짜'] = df['날짜'].astype(str).str.strip()

# 날짜 변환
df['날짜'] = pd.to_datetime(
    df['날짜'],
    errors='coerce'
)

# 날짜 오류 제거
df = df.dropna(subset=['날짜'])

# 연/월/일 생성
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# 제목
st.title("서울 기온 분석")

# 선택
month = st.selectbox("월 선택", range(1, 13))
day = st.selectbox("일 선택", range(1, 32))

# 데이터 필터
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

# 결측 제거
filtered = filtered.dropna(
    subset=['최고기온(℃)', '최저기온(℃)']
)

# 그래프
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    filtered['연도'],
    filtered['최고기온(℃)'],
    color='hotpink',
    linewidth=2,
    label='최고기온'
)

ax.plot(
    filtered['연도'],
    filtered['최저기온(℃)'],
    color='lightblue',
    linewidth=2,
    label='최저기온'
)

ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.set_title(f"{month}월 {day}일 연도별 기온 변화")

ax.legend()
ax.grid(True)

st.pyplot(fig)
