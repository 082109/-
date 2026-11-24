
import streamlit as st

st.set_page_config(
    page_title="경사하강법의 실제 활용",
    page_icon="📌",
    layout="wide"
)

# -------------------------------
# 디자인
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 4rem;
    max-width: 1100px;
}

h1, h2, h3, p, li {
    color: white;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.sub-title {
    color: #aaaaaa;
    font-size: 17px;
    margin-bottom: 45px;
}

.section-title {
    font-size: 27px;
    font-weight: 750;
    margin-top: 55px;
    margin-bottom: 20px;
}

.section-number {
    color: #ff625e;
    font-weight: bold;
    font-size: 15px;
}

.example-card {
    background-color: #1d1d1d;
    border: 1px solid #333333;
    border-radius: 13px;
    padding: 22px;
    min-height: 175px;
    margin-bottom: 12px;
}

.example-card h3 {
    font-size: 19px;
    margin-bottom: 12px;
}

.example-card p {
    color: #bbbbbb;
    font-size: 14px;
    line-height: 1.8;
}

.explain-box {
    background-color: #202020;
    border: 1px solid #393939;
    border-radius: 12px;
    padding: 24px;
    line-height: 1.9;
    margin-top: 15px;
    margin-bottom: 20px;
}

.highlight {
    color: #ff625e;
    font-weight: bold;
}

.step-card {
    background-color: #1d1d1d;
    border-left: 4px solid #ff625e;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 12px;
}

.step-card p {
    color: #cccccc;
    margin-bottom: 0;
    line-height: 1.8;
}

hr {
    border-color: #333333;
    margin-top: 35px;
    margin-bottom: 35px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# 제목
# -------------------------------
st.markdown(
    '<div class="main-title">경사하강법의 실제 활용</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">다양한 인공지능 기술 속 경사하강법</div>',
    unsafe_allow_html=True
)


# -------------------------------
# 01. 경사하강법 활용 사례
# -------------------------------
st.markdown(
    '<div class="section-number">01 / APPLICATION</div>'
    '<div class="section-title">경사하강법은 어디에 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "경사하강법은 다양한 인공지능 모델을 학습시키는 과정에서 "
    "예측 오차를 줄이는 데 활용된다. "
    "대표적인 활용 사례를 살펴보자."
)

examples = [
    (
        "🖼️ 이미지 인식",
        "사진 속 사물이 무엇인지 구별하는 인공지능을 학습시킬 때 활용된다. "
        "예를 들어 고양이와 강아지 사진을 구분하는 과정에서 "
        "잘못 분류한 결과를 줄이도록 모델을 조정한다."
    ),
    (
        "🎙️ 음성 인식",
        "사람의 음성을 문자로 변환하는 기술에 활용된다. "
        "음성을 분석해 문장을 예측하고, 실제 문장과의 차이를 줄이도록 학습한다."
    ),
    (
        "🌐 기계 번역",
        "한 언어의 문장을 다른 언어로 번역하는 인공지능에 활용된다. "
        "번역 결과가 정답 문장과 가까워지도록 모델을 학습시킨다."
    ),
    (
        "🎬 콘텐츠 추천",
        "영상 플랫폼에서 사용자가 관심을 가질 만한 콘텐츠를 예측하는 모델에 활용된다. "
        "사용자의 반응과 예측 결과 사이의 오차를 줄이도록 학습한다."
    ),
    (
        "💬 감정 분석",
        "댓글이나 게시글이 긍정적인지 부정적인지 판단하는 인공지능에 활용된다. "
        "감정 분류 결과가 실제 정답과 가까워지도록 모델을 조정한다."
    ),
    (
        "🚗 자율주행",
        "주변 차량과 보행자, 도로 상황 등을 인식하는 인공지능 모델의 "
        "학습 과정에서 예측 오차를 줄이는 데 활용될 수 있다."
    )
]

cols = st.columns(3)

for i, (title, description) in enumerate(examples):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="example-card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# -------------------------------
# 02. 콘텐츠 추천 알고리즘
# -------------------------------
st.markdown(
    '<div class="section-number">02 / CONTENT RECOMMENDATION</div>'
    '<div class="section-title">영상 플랫폼에서는 어떻게 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "이번에는 영상 플랫폼의 콘텐츠 추천 기능을 자세히 살펴보자."
)

st.markdown("""
<div class="explain-box">
    영상 플랫폼은 사용자의 시청 기록, 좋아요, 시청 시간,
    자주 보는 영상의 분야 등을 분석한다.<br><br>

    이러한 정보를 바탕으로 사용자가 어떤 영상에 관심을 가질지 예측한다.
    이때 인공지능 모델이 실제 사용자의 반응을 정확하게 예측하도록
    학습시키는 과정에서 경사하강법이 활용될 수 있다.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 추천 알고리즘의 학습 과정
# -------------------------------
st.markdown("### 콘텐츠 추천 모델의 학습 과정")

steps = [
    (
        "STEP 1. 사용자 정보 수집",
        "사용자가 어떤 영상을 시청했는지, 어떤 영상에 좋아요를 눌렀는지 등의 정보를 모은다."
    ),
    (
        "STEP 2. 관심도 예측",
        "수집한 정보를 바탕으로 사용자가 특정 영상에 관심을 가질 가능성을 예측한다."
    ),
    (
        "STEP 3. 실제 반응과 비교",
        "모델이 예측한 결과를 실제 시청이나 클릭 등의 반응과 비교한다."
    ),
    (
        "STEP 4. 예측 오차 줄이기",
        "예측 결과와 실제 반응의 차이를 줄이기 위해 경사하강법으로 모델의 설정값을 조정한다."
    ),
    (
        "STEP 5. 반복 학습",
        "이 과정을 반복하면서 사용자의 반응을 더 잘 예측할 수 있도록 모델을 학습시킨다."
    )
]

for title, description in steps:
    st.markdown(f"""
    <div class="step-card">
        <b class="highlight">{title}</b>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# 03. 실제 적용의 의미
# -------------------------------
st.markdown(
    '<div class="section-number">03 / WHY IT MATTERS</div>'
    '<div class="section-title">반복 학습은 어떤 변화를 만들까?</div>',
    unsafe_allow_html=True
)

st.write(
    "경사하강법을 활용한 학습은 한 번의 예측으로 끝나지 않는다. "
    "모델은 예측과 실제 반응의 차이를 확인하고, "
    "그 차이를 줄이는 방향으로 여러 번 조정된다."
)

st.markdown("""
<div class="explain-box">
    <b>학습 전</b><br>
    사용자가 어떤 영상에 관심을 가질지 정확하게 예측하지 못할 수 있다.<br><br>

    <b>학습 과정</b><br>
    실제 반응과 예측 결과를 비교하고, 경사하강법으로 모델을 반복해서 조정한다.<br><br>

    <b>학습 후</b><br>
    학습 과정에서 발견한 패턴을 바탕으로 사용자가 관심을 가질 만한 콘텐츠를
    더 잘 예측할 수 있게 된다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="explain-box">
    <span class="highlight">핵심 정리</span><br><br>
    경사하강법은 영상을 직접 선택하는 기술이 아니라,
    영상에 대한 사용자의 반응을 더 정확하게 예측하도록
    추천 모델을 학습시키는 데 활용되는 방법이다.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 04. 느낀점
# -------------------------------
st.markdown(
    '<div class="section-number">04 / REFLECTION</div>'
    '<div class="section-title">느낀점</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="explain-box">
    경사하강법이 이미지 인식, 음성 인식, 콘텐츠 추천 등
    다양한 인공지능 기술의 학습 과정에 활용된다는 점을 알게 되었다.
    특히 평소 자주 사용하는 영상 플랫폼의 콘텐츠 추천 기능에도
    이러한 수학적 원리가 적용될 수 있다는 사실이 흥미로웠다.
    처음에는 경사하강법을 단순한 수학적 계산 방법으로 생각했지만,
    실제 인공지능이 예측 오차를 줄이고 학습하는 과정과 연결해 살펴보면서
    수학이 기술의 발전에 어떻게 활용되는지 이해할 수 있었다.
</div>
""", unsafe_allow_html=True)
