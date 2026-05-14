# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Country MBTI Analysis",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

mbti_columns = [col for col in df.columns if col != "Country"]

# -----------------------------
# 사이드바
# -----------------------------
st.sidebar.title("🌍 국가 선택")

selected_country = st.sidebar.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

# -----------------------------
# 선택 국가 데이터
# -----------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_values = country_data[mbti_columns].sort_values(ascending=False)

chart_df = pd.DataFrame({
    "MBTI": mbti_values.index,
    "Ratio": mbti_values.values
})

# -----------------------------
# 색상 설정
# -----------------------------
# 1등 = 진한 파랑
# 2등 = 빨강
# 나머지 = 파랑 그라데이션

blue_gradient = px.colors.sequential.Blues

colors = []

for i in range(len(chart_df)):
    if i == 1:
        colors.append("red")
    else:
        gradient_index = min(
            int((i / len(chart_df)) * (len(blue_gradient)-1)),
            len(blue_gradient)-1
        )
        colors.append(blue_gradient[::-1][gradient_index])

# -----------------------------
# Plotly 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=chart_df["MBTI"],
        y=chart_df["Ratio"],
        marker_color=colors,
        text=[f"{v:.1%}" for v in chart_df["Ratio"]],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

fig.update_layout(
    title=f"{selected_country} MBTI Distribution",
    title_x=0.5,
    height=650,
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(size=15),
    xaxis=dict(
        title="MBTI Type",
        showgrid=False
    ),
    yaxis=dict(
        title="Ratio",
        tickformat=".0%",
        gridcolor="rgba(200,200,200,0.3)"
    ),
    bargap=0.25
)

# -----------------------------
# 화면 출력
# -----------------------------
st.title("🌎 국가별 MBTI 분석 대시보드")

st.markdown(
    """
    국가를 선택하면 해당 국가의 MBTI 비율을 인터랙티브 그래프로 보여줍니다.
    
    - 🔵 대부분 유형 → 파란색 그라데이션
    - 🔴 2위 유형 → 빨간색 강조
    """
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 추가 통계
# -----------------------------
top_mbti = chart_df.iloc[0]
second_mbti = chart_df.iloc[1]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "1위 MBTI",
        top_mbti["MBTI"],
        f"{top_mbti['Ratio']:.1%}"
    )

with col2:
    st.metric(
        "2위 MBTI",
        second_mbti["MBTI"],
        f"{second_mbti['Ratio']:.1%}"
    )

# -----------------------------
# 데이터 테이블
# -----------------------------
with st.expander("데이터 보기"):
    st.dataframe(chart_df, use_container_width=True)
