# pages/03_서울관광.py

import streamlit as st
import folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("관광지 마커를 클릭하면 가까운 지하철역과 놀거리를 볼 수 있어요!")

# 관광지 데이터
places = [
    ["경복궁", 37.5796, 126.9770, "경복궁역 3호선", "한복체험, 궁궐 산책, 북촌 한옥마을"],
    ["N서울타워", 37.5512, 126.9882, "명동역 4호선", "야경 감상, 케이블카, 사랑의 자물쇠"],
    ["명동", 37.5636, 126.9827, "명동역 4호선", "쇼핑, 길거리 음식, 화장품 투어"],
    ["홍대거리", 37.5563, 126.9220, "홍대입구역 2호선", "버스킹, 카페투어, 쇼핑"],
    ["롯데월드타워", 37.5131, 127.1025, "잠실역 2호선", "서울스카이, 롯데월드, 아쿠아리움"],
    ["북촌 한옥마을", 37.5826, 126.9830, "안국역 3호선", "전통 한옥, 감성 카페"],
    ["DDP", 37.5665, 127.0092, "동대문역사문화공원역", "야경, 전시회, 쇼핑"],
    ["코엑스", 37.5125, 127.0588, "삼성역 2호선", "별마당도서관, 쇼핑몰, 맛집"],
    ["익선동", 37.5744, 126.9895, "종로3가역", "한옥거리, 감성카페"],
    ["한강공원", 37.5206, 126.9393, "여의나루역 5호선", "피크닉, 자전거, 치킨"]
]

# 컬러 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 관광지 마커 추가
for place in places:

    popup_html = f"""
    <div style="width:220px">
        <h4 style="color:#ff4b4b;">📍 {place[0]}</h4>
        <b>🚇 가까운 역</b><br>
        {place[3]}<br><br>

        <b>🎈 놀거리</b><br>
        {place[4]}
    </div>
    """

    folium.Marker(
        location=[place[1], place[2]],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=place[0],
        icon=folium.Icon(
            color="red",
            icon="star"
        )
    ).add_to(m)

# 지도 HTML 출력
map_html = m._repr_html_()

# 컬러 지도 표시
st.components.v1.html(
    map_html,
    height=700
)

st.markdown("---")

st.subheader("📍 서울 관광지 TOP10 요약")

for place in places:
    st.markdown(
        f"""
        ### 🌟 {place[0]}
        🚇 가까운 역: **{place[3]}**  
        🎈 놀거리: {place[4]}
        """
    )
