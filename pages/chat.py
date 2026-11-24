
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

h1, h2, h3, p, label {
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
    min-height: 190px;
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

.highlight {
    color: #ff625e;
    font-weight: bold;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #393939;
    border-radius: 12px;
    background-color: #202020;
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
# 01. 활용 사례
# -------------------------------
st.markdown(
    '<div class="section-number">01 / APPLICATION</div>'
    '<div class="section-title">경사하강법은 어디에 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "경사하강법은 인공지능 모델을 학습시키는 과정에서 "
    "예측 오차를 줄이는 데 활용된다. 다양한 활용 사례를 살펴보자."
)

examples = [
    (
        "🖼️ 이미지 인식",
        "고양이와 강아지 사진을 구별하는 인공지능을 학습시킬 때 활용된다. "
        "이미지를 잘못 분류한 결과를 줄이도록 모델을 조정한다."
    ),
    (
        "🎙️ 음성 인식",
        "사람의 음성을 문자로 변환하는 기술에 활용된다. "
        "음성을 분석해 예측한 문장과 실제 문장의 차이를 줄이도록 학습한다."
    ),
    (
        "🌐 기계 번역",
        "한 언어의 문장을 다른 언어로 번역하는 인공지능에 활용된다. "
        "번역 결과가 정답 문장에 가까워지도록 모델을 학습시킨다."
    ),
    (
        "🎬 콘텐츠 추천",
        "사용자의 시청 기록과 선호도를 바탕으로 관심 있을 만한 영상을 예측한다. "
        "예측 결과와 실제 반응의 차이를 줄이는 데 활용된다."
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
        st.markdown(
            f"""
            <div class="example-card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# -------------------------------
# 02. 콘텐츠 추천 사례
# -------------------------------
st.markdown(
    '<div class="section-number">02 / CONTENT RECOMMENDATION</div>'
    '<div class="section-title">영상 플랫폼에서는 어떻게 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "이번에는 영상 플랫폼에서 사용자의 관심사를 예측하는 과정을 살펴보자."
)

with st.container(border=True):
    st.subheader("사용자 정보 수집")

    st.write(
        "영상 플랫폼은 사용자가 시청한 영상, 좋아요를 누른 콘텐츠, "
        "시청 시간, 자주 보는 영상의 분야 등을 분석한다."
    )

    st.divider()

    st.subheader("관심 콘텐츠 예측")

    st.write(
        "수집한 정보를 바탕으로 사용자가 어떤 영상에 관심을 가질지 예측한다."
    )

    st.divider()

    st.subheader("실제 반응과 비교")

    st.write(
        "모델이 예측한 결과를 사용자의 실제 시청이나 클릭 등의 반응과 비교한다."
    )

    st.divider()

    st.subheader("모델 학습")

    st.write(
        "예측과 실제 반응 사이의 차이를 줄이도록 경사하강법을 이용해 "
        "모델의 설정값을 조정한다."
    )


# -------------------------------
# 03. 반복 학습의 변화
# -------------------------------
st.markdown(
    '<div class="section-number">03 / LEARNING PROCESS</div>'
    '<div class="section-title">반복 학습은 어떤 변화를 만들까?</div>',
    unsafe_allow_html=True
)

st.write(
    "경사하강법을 활용한 학습은 한 번의 예측으로 끝나지 않는다. "
    "모델은 예측과 실제 반응의 차이를 확인하고, "
    "그 차이를 줄이는 방향으로 여러 번 조정된다."
)

with st.container(border=True):
    st.subheader("학습 전")

    st.write(
        "사용자가 어떤 영상에 관심을 가질지 "
        "정확하게 예측하지 못할 수 있다."
    )

    st.divider()

    st.subheader("학습 과정")

    st.write(
        "실제 반응과 예측 결과를 비교하고, "
        "경사하강법으로 모델의 설정값을 반복해서 조정한다."
    )

    st.divider()

    st.subheader("학습 후")

    st.write(
        "학습 과정에서 발견한 패턴을 바탕으로 "
        "사용자가 관심을 가질 만한 콘텐츠를 더 잘 예측할 수 있게 된다."
    )

with st.container(border=True):
    st.markdown(
        '<p class="highlight">핵심 정리</p>',
        unsafe_allow_html=True
    )

    st.write(
        "경사하강법은 영상을 직접 선택하는 기술이 아니라, "
        "영상에 대한 사용자의 반응을 더 정확하게 예측하도록 "
        "추천 모델을 학습시키는 데 활용되는 방법이다."
    )


# -------------------------------
# 04. 느낀점
# -------------------------------
st.markdown(
    '<div class="section-number">04 / REFLECTION</div>'
    '<div class="section-title">느낀점</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.write(
        "경사하강법이 이미지 인식, 음성 인식, 콘텐츠 추천 등 "
        "다양한 인공지능 기술의 학습 과정에 활용된다는 점을 알게 되었다. "
        "특히 평소 자주 사용하는 영상 플랫폼의 콘텐츠 추천 기능에도 "
        "이러한 수학적 원리가 적용될 수 있다는 사실이 흥미로웠다. "
        "처음에는 경사하강법을 단순한 수학적 계산 방법으로 생각했지만, "
        "실제 인공지능이 예측 오차를 줄이고 학습하는 과정과 연결해 살펴보면서 "
        "수학이 기술의 발전에 어떻게 활용되는지 이해할 수 있었다."
    )
