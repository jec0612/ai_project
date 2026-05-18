import streamlit as st
import folium

st.set_page_config(page_title="서울 관광지", layout="wide")

st.title("🌏 서울 관광지 TOP10")

places = [
    ["경복궁", 37.5796, 126.9770, "경복궁역", "한복체험, 북촌한옥마을"],
    ["N서울타워", 37.5512, 126.9882, "명동역", "야경, 케이블카"],
    ["명동", 37.5636, 126.9827, "명동역", "쇼핑, 길거리 음식"],
]

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for place in places:
    folium.Marker(
        [place[1], place[2]],
        popup=f"""
        <b>{place[0]}</b><br>
        🚇 {place[3]}<br>
        🎈 {place[4]}
        """,
    ).add_to(m)

html_string = m._repr_html_()

st.components.v1.html(html_string, height=600)
