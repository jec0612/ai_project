import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="날씨별 음료 추천 프로그램",
    page_icon="☕",
    layout="centered"
)

# -----------------------------
# 제목
# -----------------------------
st.title("☕ 날씨별 음료 추천 프로그램")
st.write("기상청 데이터를 활용하여 기온에 맞는 음료를 추천하는 프로그램입니다.")

# -----------------------------
# CSV 파일 불러오기
# -----------------------------
# 업로드한 기상청 CSV 파일 이름
file_path = 'ta_20260601110744.csv'

# 기상청 CSV는 위쪽 설명 부분이 있어서 skiprows 사용
try:
    df = pd.read_csv(file_path, encoding='cp949', skiprows=7)

    # 날짜 앞 공백 제거
    df['날짜'] = df['날짜'].astype(str).str.strip()

    # 날짜 형식 변환
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 월 추출
    df['월'] = df['날짜'].dt.month

except Exception as e:
    st.error(f'CSV 파일을 불러오는 중 오류가 발생했습니다: {e}')
    st.stop()

# -----------------------------
# 현재 기온 입력
# -----------------------------
st.subheader('🌡 현재 기온 입력')

current_temp = st.slider(
    '현재 기온을 선택하세요',
    min_value=-10,
    max_value=40,
    value=20
)

# -----------------------------
# 음료 추천 로직
# -----------------------------
if current_temp >= 30:
    drink = '🥤 아이스 아메리카노'
    message = '매우 더운 날씨에는 시원한 커피가 잘 어울립니다!'

elif current_temp >= 23:
    drink = '🍹 아이스티'
    message = '더운 날씨에는 상큼한 음료를 추천합니다!'

elif current_temp >= 15:
    drink = '☕ 카페라떼'
    message = '선선한 날씨에는 부드러운 라떼가 잘 어울립니다!'

elif current_temp >= 5:
    drink = '🍵 따뜻한 녹차'
    message = '쌀쌀한 날씨에는 따뜻한 차가 좋습니다!'

else:
    drink = '🍫 핫초코'
    message = '추운 날씨에는 달콤한 핫초코를 추천합니다!'

# -----------------------------
# 추천 결과 출력
# -----------------------------
st.subheader('✅ 추천 결과')

st.success(f'현재 추천 음료: {drink}')
st.write(message)

# -----------------------------
# 계절별 특징 설명
# -----------------------------
st.subheader('📌 계절별 음료 특징')

st.markdown('''
- 여름에는 차가운 음료 소비가 증가합니다.
- 겨울에는 따뜻한 음료 소비가 증가합니다.
- 봄과 가을에는 라떼와 차 종류가 인기가 많습니다.
''')

# -----------------------------
# 월별 평균기온 계산
# -----------------------------
monthly_temp = df.groupby('월')['평균기온(℃)'].mean().reset_index()

# -----------------------------
# 그래프 출력
# -----------------------------
st.subheader('📈 월별 평균 기온 그래프')

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    monthly_temp['월'],
    monthly_temp['평균기온(℃)'],
    marker='o',
    linewidth=2
)

ax.set_xlabel('월')
ax.set_ylabel('평균기온(℃)')
ax.set_title('서울 월별 평균 기온')

st.pyplot(fig)

# -----------------------------
# 데이터 표 출력
# -----------------------------
st.subheader('📋 기상청 데이터')

st.dataframe(df, use_container_width=True)

# -----------------------------
# 최종 설명
# -----------------------------
st.info(
    '이 프로그램은 기상청 데이터를 활용하여 기온에 따라 어울리는 음료를 추천합니다.'
)
