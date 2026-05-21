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
df = pd.read_csv("population.csv", encoding="cp949")

# 숫자 변환 함수
def to_num(x):
    return int(str(x).replace(",", ""))

# 총인구수 컬럼 숫자 변환
df["2026년04월_거주자_총인구수"] = df["2026년04월_거주자_총인구수"].apply(to_num)

# 행정구 목록
districts = df["행정구역"].tolist()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("서울시 행정구별 인구수")

selected = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택된 구 데이터
row = df[df["행정구역"] == selected].iloc[0]

# 연령대 컬럼
age_columns = [
    "2026년04월_거주자_0~9세",
    "2026년04월_거주자_10~19세",
    "2026년04월_거주자_20~29세",
    "2026년04월_거주자_30~39세",
    "2026년04월_거주자_40~49세",
    "2026년04월_거주자_50~59세",
    "2026년04월_거주자_60~69세",
    "2026년04월_거주자_70~79세",
    "2026년04월_거주자_80~89세",
    "2026년04월_거주자_90~99세",
    "2026년04월_거주자_100세 이상"
]

# 나이 라벨
ages = [
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70~79세",
    "80~89세",
    "90~99세",
    "100세 이상"
]

# 인구수 데이터
population = [to_num(row[col]) for col in age_columns]

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# 회색 배경
fig.patch.set_facecolor("lightgray")
ax.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax.plot(
    ages,
    population,
    color="red",
    marker="o",
    linewidth=3
)

# 제목 및 축
ax.set_title("서울시 행정구별 인구수", fontsize=18)
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# 격자
ax.grid(True)

# Streamlit 출력
st.pyplot(fig)
