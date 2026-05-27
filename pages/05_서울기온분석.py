import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("seoul.csv", encoding='cp949')

# 컬럼 이름 정리
df.columns = df.columns.str.strip()

# 날짜 형식 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 연도 / 월 / 일 컬럼 생성
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# -----------------------------
# Streamlit 제목
# -----------------------------
st.title("서울 기온 데이터 분석")

st.write("월과 일을 선택하면 연도별 최고/최저기온 변화를 보여줍니다.")

# -----------------------------
# 월 / 일 선택
# -----------------------------
month = st.selectbox("월 선택", range(1, 13))
day = st.selectbox("일 선택", range(1, 32))

# -----------------------------
# 선택 날짜 데이터 추출
# -----------------------------
filtered = df[(df['월'] == month) & (df['일'] == day)]

# 결측치 제거
filtered = filtered.dropna(subset=['최고기온(℃)', '최저기온(℃)'])

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    filtered['연도'],
    filtered['최고기온(℃)'],
    color='hotpink',
    label='최고기온',
    linewidth=2
)

ax.plot(
    filtered['연도'],
    filtered['최저기온(℃)'],
    color='lightblue',
    label='최저기온',
    linewidth=2
)

ax.set_title(f"{month}월 {day}일의 연도별 최고/최저기온")
ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.legend()
ax.grid(True)

st.pyplot(fig)
