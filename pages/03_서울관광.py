# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("지도의 마커를 클릭하면 가까운 지하철역과 놀거리를 확인할 수 있어요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "경복궁역 3호선",
        "fun": "한복 체험, 궁궐 산책, 북촌 한옥마을"
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역 4호선",
        "fun": "야경 감상, 케이블카, 사랑의 자물쇠"
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9827,
        "station": "명동역 4호선",
        "fun": "쇼핑, 길거리 음식, 화장품 투어"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "홍대입구역 2호선",
        "fun": "버스킹, 카페투어, 쇼핑"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역 2호선",
        "fun": "서울스카이, 롯데월드, 아쿠아리움"
    },
    {
        "name": "북촌 한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역 3호선",
        "fun": "전통 한옥 구경, 사진 촬영, 전통 카페"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": "야경, 전시회, 쇼핑"
    },
    {
        "name": "코엑스",
        "lat": 37.5125,
        "lon": 127.0588,
        "station": "삼성역 2호선",
        "fun": "별마당도서관, 쇼핑몰, 맛집"
    },
    {
        "name": "익선동",
        "lat": 37.5744,
        "lon": 126.9895,
        "station": "종로3가역",
        "fun": "감성 카페, 한옥거리, 맛집 탐방"
    },
    {
        "name": "한강공원",
        "lat": 37.5206,
        "lon": 126.9393,
        "station": "여의나루역 5호선",
        "fun": "치킨 먹기, 자전거, 피크닉"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    popup_text = f"""
    <b>{place['name']}</b><br>
    🚇 가까운 역: {place['station']}<br>
    🎈 놀거리: {place['fun']}
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(
    m,
    width=1200,
    height=600
)

# 클릭 정보 표시
st.markdown("---")
st.subheader("📍 관광지 정보")

clicked = map_data.get("last_object_clicked_tooltip")

if clicked:
    selected = next((p for p in places if p["name"] == clicked), None)

    if selected:
        st.success(
            f"🚇 가까운 역: {selected['station']} | 🎈 놀거리: {selected['fun']}"
        )
else:
    st.info("지도의 관광지를 클릭해보세요!")
