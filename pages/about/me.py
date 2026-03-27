import streamlit as st

def show_profile():
    st.title("👨‍💻 About Me")
    
    # 상단 프로필 영역 (컬럼 분할)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 프로필 이미지 (원하는 이미지 URL이나 파일 경로로 수정하세요)
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=Felix", width=200)
        
    with col2:
        st.header("안녕하세요! 끊임없이 성장하는 예비 소프트웨어 엔지니어입니다.")
        st.write("""
        컴퓨터 공학을 전공하였고, 현재는 튼튼한 백엔드 아키텍처와 데이터 분석에 푹 빠져 있습니다.
        가성비와 실용성을 중요하게 생각하며, 일상 속의 불편함을 해결하는 소프트웨어 기획에 관심이 많습니다.
        앞으로 전문적인 기술을 결합하여 더 나은 가치를 창출하는 개발자로 도약하는 것을 목표로 하고 있습니다.
        """)

    st.divider()

    # 기술 스택 & 학습 현황
    st.subheader("🛠️ Tech Stack & Current Focus")
    st.write("""
    * **Backend:** Java, Spring MVC (김영한님 강의로 깊이 있게 학습 중!)
    * **Data/AI:** Python, Pandas (국비 지원 아카데미 수강 중)
    * **Environment:** 독산동의 작업실에서 코딩 중 (최근 마련한 코어 울트라 5 탑재 레노버 아이디어패드 애용 중 💻)
    """)

    # 취미 & 관심사
    st.subheader("🧸 Interests & Lifestyle")
    st.write("""
    * **수집:** 카카오프렌즈(특히 춘식이와 라이언!) 인형을 바자회나 중고 마켓에서 모으는 것을 즐깁니다.
    * **여행:** 무궁화호를 타고 여유롭게 떠나는 가성비 기차 여행을 좋아합니다.
    * **미디어:** 가끔은 '서른이지만 열일곱입니다' 같은 로맨스 드라마를 보며 힐링하는 시간을 가집니다.
    """)

    st.divider()

    # 연락처 및 소셜 링크
    st.subheader("🔗 Connect with me")
    
    # 인스타그램, 깃허브 등 실제 본인의 링크로 수정해주세요.
    st.markdown("""
    [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ddungsaeng)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jjune960)
    [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jjune960@gmail.com)
    """)