import streamlit as st


def show_sns_banners():
    st.title("SNS 광고 배너 기획안 (일본 여행 취향)")
    st.caption("아래 3개는 이 프로젝트(일본 여행 설문/대시보드) 기준으로 바로 디자이너가 제작할 수 있게 카피/구성/가이드를 정리했습니다.")

    banners = [
        {
            "name": "배너 1: 1분 설문 참여형",
            "format_hint": "인스타 피드/스토리 모두 대응(가로형도 가능)",
            "main": "일본 여행 취향, 1분 설문으로 알아보기",
            "sub": "선택한 답을 바탕으로 취향을 시각화한 리포트를 보여드려요.",
            "cta": "설문 시작하기",
            "fineprint": "중복 참여 방지(프로젝트 로직 기준)",
            "designer_guide": {
                "비주얼": "미니 체크리스트(3단계 느낌) + 지도/노선 추상 라인",
                "컬러": "화이트 배경 + 포인트 컬러(레드/블루 톤) 1개만 강하게",
                "타이포": "메인 카피는 굵은 산세리프, 서브는 얇게",
                "레이아웃": "상단 메인 문구 → 중앙 포인트 아이콘/그래픽 → 하단 CTA 버튼",
            },
        },
        {
            "name": "배너 2: AI 분석 기대감(대시보드로 연결)",
            "format_hint": "그래프 감성(도넛/막대) 오버레이 추천",
            "main": "AI가 정리하는 일본 여행 취향 리포트",
            "sub": "문항별 요약 + 차트 대시보드로 한눈에 확인하세요.",
            "cta": "대시보드 확인하기",
            "fineprint": "AI Prediction은 준비 중이지만, 결과 대시보드는 바로 제공됩니다.",
            "designer_guide": {
                "비주얼": "반투명 그래프(도넛/막대) + 네온 글로우(과하지 않게)",
                "컬러": "다크 톤 또는 오프화이트 배경 중 택1 + 포인트 1색",
                "타이포": "리포트/대시보드 같은 키워드만 더 크게 강조",
                "레이아웃": "좌측 텍스트 + 우측 그래프 배경(겹침) 구성",
            },
        },
        {
            "name": "배너 3: 결과 즉시 보기(저장/공유 유도)",
            "format_hint": "모달/카드 느낌으로 ‘바로 본다’ 강조",
            "main": "내 취향 결과, 지금 바로 대시보드로",
            "sub": "문항별 요약 테이블 + 시각화 차트 한 화면에 정리.",
            "cta": "결과 보기",
            "fineprint": "설문 후 즉시 확인(데이터 로드 상태에 따라 표시)",
            "designer_guide": {
                "비주얼": "대시보드 스크린샷 목업(텍스트/차트 블록 형태) 1장",
                "컬러": "선명한 차트 컬러 3~4개 + 깔끔한 흰 배경",
                "타이포": "메인 문구는 2줄 이내로 압축",
                "레이아웃": "상단 타이틀 → 중앙 목업 → 하단 CTA 버튼",
            },
        },
    ]

    tabs = st.tabs([b["name"] for b in banners])

    for tab, banner in zip(tabs, banners):
        with tab:
            st.subheader(banner["name"])

            st.markdown("**메인 문구**")
            st.code(banner["main"])
            st.markdown("**서브 문구**")
            st.code(banner["sub"])
            st.markdown("**CTA 버튼**")
            st.code(banner["cta"])
            st.markdown("**작은 문구(고지/하단 텍스트)**")
            st.code(banner["fineprint"])

            with st.expander("디자인 가이드 (디자이너용)"):
                st.write(f"추천 포맷: {banner['format_hint']}")
                for k, v in banner["designer_guide"].items():
                    st.write(f"- {k}: {v}")


if __name__ == "__main__":
    show_sns_banners()

