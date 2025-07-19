
import streamlit as st
import time
import random

# 페이지 구성 설정
st.set_page_config(page_title="수출 프로젝트 실시간 진행률", layout="wide")
st.title("📊 수출 프로젝트 실시간 진행 상황 (모의 데이터 기반)")

# 항목 리스트
categories = [
    "HS코드 전체 분석",
    "식품 리포트 (20개국)",
    "의료기기 리포트",
    "친환경 전력장비",
    "10개 카테고리 리포트",
    "DM/이메일 커스터마이징",
    "전체 ZIP 파일 생성"
]

# 초기 진행률 설정 (0~100 사이 랜덤 시작값)
progress_values = {cat: random.uniform(0, 30) for cat in categories}

st.subheader("⏱ 실시간 자동 갱신 (1초마다 진행률 시뮬레이션)")
placeholder = st.empty()

# 진행률 시뮬레이션 및 시각화
for _ in range(1000):
    with placeholder.container():
        for cat in categories:
            if progress_values[cat] < 100:
                progress_values[cat] = min(progress_values[cat] + random.uniform(0.2, 0.8), 100.0)
            st.progress(progress_values[cat] / 100.0, text=f"{cat}: {progress_values[cat]:.3f}%")
    time.sleep(1)
