
import streamlit as st
import time
import requests

# 페이지 구성 설정
st.set_page_config(page_title="수출 프로젝트 실시간 진행률", layout="wide")
st.title("📊 수출 프로젝트 실시간 진행 상황 (API 연동)")

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

# API 엔드포인트 설정 (예시 URL, 실제 환경에 맞게 수정)
API_URL = "http://yourserver.com/api/progress"  # 실제 진행률 JSON 제공 URL

st.subheader("⏱ 실시간 API 기반 자동 갱신 (1초마다)")
placeholder = st.empty()

# 진행률 요청 및 시각화
for _ in range(1000):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()  # 예: {"HS코드 전체 분석": 87.5, ...}
        else:
            data = {}
    except:
        data = {}

    with placeholder.container():
        for cat in categories:
            value = data.get(cat, 0.0)
            st.progress(value / 100.0, text=f"{cat}: {value:.3f}%")

    time.sleep(1)
