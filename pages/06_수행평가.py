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
    if i % 2 == 0:
        with col1:
            st.markdown(f'''
            <div style="
                background-color:#fff4e6;
                padding:15px;
                margin-bottom:10px;
                border-radius:15px;
                text-align:center;
                font-size:20px;
                font-weight:bold;
            ">
                {drink}
            </div>
            ''', unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(f'''
            <div style="
                background-color:#e8f7ff;
                padding:15px;
                margin-bottom:10px;
                border-radius:15px;
                text-align:center;
                font-size:20px;
                font-weight:bold;
            ">
                {drink}
            </div>
            ''', unsafe_allow_html=True)

# -----------------------------
# 음료 설명 데이터
# -----------------------------
drink_info = {
    '🥤 아이스 아메리카노': {
        '맛': '쓴맛과 시원한 맛',
        '효과': '졸음을 깨우고 집중력을 높여줍니다.'
    },
    '🍹 레몬에이드': {
        '맛': '상큼하고 달콤한 맛',
        '효과': '피로 회복과 갈증 해소에 도움을 줍니다.'
    },
    '🧃 오렌지주스': {
        '맛': '달콤하고 새콤한 맛',
        '효과': '비타민C 보충에 좋습니다.'
    },
    '🧊 콜라': {
        '맛': '톡 쏘는 탄산 맛',
        '효과': '청량감을 느끼게 해줍니다.'
    },
    '⚡ 스포츠음료': {
        '맛': '달콤하고 시원한 맛',
        '효과': '수분과 전해질 보충에 도움을 줍니다.'
    },
    '🥛 탄산수': {
        '맛': '깔끔하고 시원한 맛',
        '효과': '갈증 해소에 좋습니다.'
    },
    '🍹 아이스티': {
        '맛': '달콤하고 상쾌한 맛',
        '효과': '더운 날씨에 시원함을 제공합니다.'
    },
    '☕ 콜드브루': {
        '맛': '부드럽고 진한 커피 맛',
        '효과': '카페인으로 집중력을 높여줍니다.'
    },
    '🧃 사과주스': {
        '맛': '달콤한 과일 맛',
        '효과': '비타민과 수분 보충에 좋습니다.'
    },
    '🥛 요거트 음료': {
        '맛': '새콤달콤한 맛',
        '효과': '소화에 도움을 줍니다.'
    },
    '🥤 사이다': {
        '맛': '시원한 탄산 맛',
        '효과': '청량감을 느끼게 해줍니다.'
    },
    '☕ 카페라떼': {
        '맛': '부드럽고 고소한 맛',
        '효과': '편안한 느낌을 줍니다.'
    },
    '🍵 녹차': {
        '맛': '깔끔하고 은은한 맛',
        '효과': '마음을 안정시키는 데 도움을 줍니다.'
    },
    '🫖 허브티': {
        '맛': '향긋하고 부드러운 맛',
        '효과': '긴장 완화에 도움을 줍니다.'
    },
    '🥛 우유': {
        '맛': '고소하고 부드러운 맛',
        '효과': '칼슘 보충에 좋습니다.'
    },
    '🍶 두유': {
        '맛': '담백하고 고소한 맛',
        '효과': '식물성 단백질 보충에 좋습니다.'
    },
    '🍵 따뜻한 녹차': {
        '맛': '따뜻하고 깔끔한 맛',
        '효과': '몸을 따뜻하게 해줍니다.'
    },
    '☕ 아메리카노': {
        '맛': '진하고 쌉싸름한 맛',
        '효과': '집중력 향상에 도움을 줍니다.'
    },
    '🫖 홍차': {
        '맛': '진하고 향긋한 맛',
        '효과': '피로 회복에 도움을 줍니다.'
    },
    '🥛 따뜻한 우유': {
        '맛': '부드럽고 따뜻한 맛',
        '효과': '편안한 수면에 도움을 줍니다.'
    },
    '🍠 고구마라떼': {
        '맛': '달콤하고 고소한 맛',
        '효과': '포만감을 줍니다.'
    },
    '🍫 핫초코': {
        '맛': '달콤하고 진한 초콜릿 맛',
        '효과': '몸을 따뜻하게 해줍니다.'
    },
    '☕ 뜨거운 커피': {
        '맛': '따뜻하고 진한 커피 맛',
        '효과': '졸음을 깨우는 데 도움을 줍니다.'
    },
    '🫖 생강차': {
        '맛': '알싸하고 따뜻한 맛',
        '효과': '몸을 따뜻하게 해줍니다.'
    },
    '🍵 전통차': {
        '맛': '은은하고 부드러운 맛',
        '효과': '피로 회복에 도움을 줍니다.'
    },
    '🥛 따뜻한 두유': {
        '맛': '고소하고 따뜻한 맛',
        '효과': '영양 보충에 좋습니다.'
    }
}

# -----------------------------
# 음료 선택 설명
# -----------------------------
st.subheader('🧋 음료 상세 설명')

selected_drink = st.selectbox(
    '궁금한 음료를 선택하세요',
    drinks
)

info = drink_info[selected_drink]

st.markdown(f'''
<div style="
    background-color:#f7f7f7;
    padding:20px;
    border-radius:15px;
    border:2px solid #dddddd;
">
    <h3>{selected_drink}</h3>
    <p><b>🍴 맛:</b> {info['맛']}</p>
    <p><b>✨ 효과:</b> {info['효과']}</p>
</div>
''', unsafe_allow_html=True)

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


