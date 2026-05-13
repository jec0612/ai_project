import streamlit as st

# MBTI별 진로 데이터
career_data = {
    "ISTJ": [
        {
            "career": "회계사",
            "major": "회계학과, 경영학과",
            "personality": "꼼꼼하고 책임감이 강하며 체계적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "career": "공무원",
            "major": "행정학과, 법학과",
            "personality": "안정적이고 성실한 성향의 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ISFJ": [
        {
            "career": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "사회복지사",
            "major": "사회복지학과",
            "personality": "공감 능력이 뛰어나고 따뜻한 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "INFJ": [
        {
            "career": "심리상담사",
            "major": "심리학과",
            "personality": "통찰력이 있고 사람의 감정을 잘 이해하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "작가",
            "major": "문예창작학과",
            "personality": "창의적이고 깊은 사고를 하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "INTJ": [
        {
            "career": "데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 전략적인 사람",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "career": "연구원",
            "major": "자연과학계열",
            "personality": "탐구심이 강하고 분석적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "ISTP": [
        {
            "career": "정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 문제 해결 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "바리스타",
            "major": "호텔조리학과, 식음료학과",
            "personality": "실무 능력이 좋고 차분한 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ISFP": [
        {
            "career": "제과제빵사",
            "major": "제과제빵학과",
            "personality": "섬세하고 감각적인 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "career": "디자이너",
            "major": "시각디자인학과",
            "personality": "예술 감각이 뛰어나고 창의적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "INFP": [
        {
            "career": "작곡가",
            "major": "실용음악과",
            "personality": "감수성이 풍부하고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "career": "웹툰 작가",
            "major": "만화애니메이션학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "INTP": [
        {
            "career": "프로그래머",
            "major": "컴퓨터공학과",
            "personality": "논리적이고 분석을 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "career": "AI 연구원",
            "major": "인공지능학과",
            "personality": "호기심이 많고 탐구형인 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ESTP": [
        {
            "career": "마케터",
            "major": "광고홍보학과",
            "personality": "활동적이고 도전적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "승무원",
            "major": "항공서비스학과",
            "personality": "사교성이 좋고 순발력 있는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],

    "ESFP": [
        {
            "career": "유튜버",
            "major": "미디어학과",
            "personality": "에너지가 넘치고 표현력이 좋은 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "career": "이벤트 플래너",
            "major": "관광경영학과",
            "personality": "사람 만나는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ENFP": [
        {
            "career": "광고기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 열정적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "career": "크리에이터",
            "major": "미디어콘텐츠학과",
            "personality": "창의적이고 활발한 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENTP": [
        {
            "career": "기업가",
            "major": "경영학과",
            "personality": "도전을 즐기고 아이디어가 많은 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "career": "변호사",
            "major": "법학과",
            "personality": "토론을 좋아하고 논리적인 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],

    "ESTJ": [
        {
            "career": "경영 관리자",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력이 있는 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "career": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "ESFJ": [
        {
            "career": "교사",
            "major": "교육학과",
            "personality": "친절하고 협동심이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "career": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENFJ": [
        {
            "career": "HR 담당자",
            "major": "경영학과",
            "personality": "사람을 잘 이끌고 공감 능력이 좋은 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "career": "강사",
            "major": "교육학과",
            "personality": "전달력이 좋고 열정적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENTJ": [
        {
            "career": "CEO",
            "major": "경영학과",
            "personality": "목표 지향적이고 리더십이 강한 사람",
            "salary": "평균 연봉 약 1억원"
        },
        {
            "career": "투자 분석가",
            "major": "경제학과",
            "personality": "분석력과 판단력이 뛰어난 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ]
}

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="✨",
    layout="centered"
)

st.title("✨ MBTI 진로 추천 프로그램")
st.write("MBTI를 선택하면 어울리는 진로 2가지를 추천해드립니다!")

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(career_data.keys())
)

# 결과 출력
if st.button("진로 추천 받기"):
    st.subheader(f"📌 {selected_mbti} 추천 진로")

    careers = career_data[selected_mbti]

    for idx, item in enumerate(careers, start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.write(f"📚 적합한 학과: {item['major']}")
        st.write(f"👤 어울리는 성격: {item['personality']}")
        st.write(f"💰 평균 연봉: {item['salary']}")
        st.divider()

st.caption("※ 연봉은 평균적인 예시이며 실제와 차이가 있을 수 있습니다.")
