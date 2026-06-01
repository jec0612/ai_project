import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title='날씨별 음료 추천 프로그램',
    page_icon='☕',
    layout='centered'
)

# -----------------------------
# 제목
# -----------------------------
st.title('☕ 날씨별 음료 추천 프로그램')
st.write('기상청 데이터를 활용하여 기온에 맞는 음료를 추천하는 프로그램입니다.')

# -----------------------------
# CSV 파일 불러오기
# -----------------------------
file_path = 'ta_20260601110744.csv'

try:
    df = pd.read_csv(file_path, encoding='cp949', skiprows=7)

    # 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 변환
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 평균기온 숫자 변환
    df['평균기온(℃)'] = pd.to_numeric(df['평균기온(℃)'], errors='coerce')

    # 결측값 제거
    df = df.dropna(subset=['평균기온(℃)'])

except Exception as e:
    st.error(f'파일 오류: {e}')
    st.stop()

# -----------------------------
# 기온 입력
# -----------------------------
st.subheader('🌡 현재 기온 입력')

current_temp = st.slider(
    '현재 기온을 선택하세요',
    -10,
    40,
    20
)

# -----------------------------
# 음료 추천
# -----------------------------
if current_temp >= 32:
    season = '여름'
    drinks = [
        '🥤 아이스 아메리카노',
        '🍹 레몬에이드',
        '🧃 오렌지주스',
        '🧊 콜라',
        '⚡ 스포츠음료',
        '🥛 탄산수'
    ]

    feature = '여름에는 시원하고 청량감 있는 음료 소비가 증가합니다.'

elif current_temp >= 24:
    season = '초여름'
    drinks = [
        '🍹 아이스티',
        '☕ 콜드브루',
        '🧃 사과주스',
        '🥛 요거트 음료',
        '🥤 사이다'
    ]

    feature = '더운 날씨에는 상큼한 과일음료와 차가운 음료가 인기가 많습니다.'

elif current_temp >= 15:
    season = '봄 / 가을'
    drinks = [
        '☕ 카페라떼',
        '🍵 녹차',
        '🫖 허브티',
        '🥛 우유',
        '🍶 두유'
    ]

    feature = '봄과 가을에는 부드럽고 따뜻한 음료 소비가 증가합니다.'

elif current_temp >= 5:
    season = '쌀쌀한 날씨'
    drinks = [
        '🍵 따뜻한 녹차',
        '☕ 아메리카노',
        '🫖 홍차',
        '🥛 따뜻한 우유',
        '🍠 고구마라떼'
    ]

    feature = '쌀쌀한 날씨에는 따뜻한 차와 커피가 잘 어울립니다.'

else:
    season = '겨울'
    drinks = [
        '🍫 핫초코',
        '☕ 뜨거운 커피',
        '🫖 생강차',
        '🍵 전통차',
        '🥛 따뜻한 두유'
    ]

    feature = '겨울에는 따뜻하고 달콤한 음료 소비가 증가합니다.'

# -----------------------------
# 추천 결과
# -----------------------------
st.subheader('✅ 추천 결과')

st.success(f'현재 계절: {season}')

st.write('### 🍹 추천 음료')

for drink in drinks:
    st.write(f'- {drink}')

# -----------------------------
# 계절 특징
# -----------------------------
st.subheader('📌 계절별 음료 특징')

st.info(feature)

# -----------------------------
# 그래프
# -----------------------------
st.subheader('📈 날짜별 평균 기온 그래프')

# 날짜순 정렬
df = df.sort_values('날짜')

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df['날짜'],
    df['평균기온(℃)'],
    marker='o',
    linewidth=2
)

ax.set_xlabel('날짜')
ax.set_ylabel('평균기온(℃)')
ax.set_title('서울 날짜별 평균 기온')

plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------
# 데이터 표
# -----------------------------
st.subheader('📋 기상청 데이터')

st.dataframe(df, use_container_width=True)

# -----------------------------
# 하단 설명
# -----------------------------
st.info('이 프로그램은 기상청 데이터를 활용하여 기온에 따라 어울리는 음료를 추천합니다.')
