# pages/03_서울관광.py

import streamlit as st
import folium
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🌏",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.caption("관광지 마커를 클릭하면 가까운 지하철역과 놀거리를 볼 수 있어요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "경복궁역 3호선",
        "fun": "한복 체험 · 북촌 한옥마을 · 궁궐 산책"
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역 4호선",
        "fun": "서울 야경 · 케이블카 · 사랑의 자물쇠"
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9827,
        "station": "명동역 4호선",
        "fun": "쇼핑 · 길거리 음식 · 화장품 투어"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "홍대입구역 2호선",
        "fun": "버스킹 · 감성카페 · 쇼핑"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역 2호선",
        "fun": "서울스카이 · 롯데월드 · 아쿠아리움"
    },
    {
        "name": "북촌 한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역 3호선",
        "fun": "전통 한옥 · 사진 명소 · 전통 카페"
    },
    {
        "name": "DDP",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": "야경 · 전시회 · 쇼핑"
    },
    {
        "name": "코엑스",
        "lat": 37.5125,
        "lon": 127.0588,
        "station": "삼성역 2호선",
        "fun": "별마당도서관 · 맛집 · 쇼핑"
    },
    {
        "name": "익선동",
        "lat": 37.5744,
        "lon": 126.9895,
        "station": "종로3가역",
        "fun": "감성카페 · 한옥거리 · 맛집"
    },
    {
        "name": "한강공원",
        "lat": 37.5206,
        "lon": 126.9393,
        "station": "여의나루역 5호선",
        "fun": "피크닉 · 자전거 · 치맥"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 클러스터
marker_cluster = MarkerCluster().add_to(m)

# 마커 추가
for place in places:
    popup_html = f"""
    <div style="width:230px;">
        <h4>{place['name']}</h4>
        <hr>
        <b>🚇 가까운 역</b><br>
        {place['station']}<br><br>

        <b>🎈 놀거리</b><br>
        {place['fun']}
    </div>
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(marker_cluster)

# 지도 출력
st.components.v1.html(
    m._repr_html_(),
    height=700
)

# 하단 정보
st.markdown("---")
st.subheader("📍 서울 관광지 TOP10")

for idx, place in enumerate(places, start=1):
    st.markdown(
        f"""
        ### {idx}. {place['name']}
        - 🚇 가까운 역: {place['station']}
        - 🎈 놀거리: {place['fun']}
        """
    )
