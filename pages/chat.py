
import streamlit as st

st.set_page_config(
    page_title="경사하강법의 실제 활용",
    page_icon="📌",
    layout="wide"
)

# -------------------------------
# 기본 디자인
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

h1, h2, h3, p, li, div {
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
    min-height: 145px;
    margin-bottom: 12px;
}

.example-card h3 {
    font-size: 19px;
    margin-bottom: 10px;
}

.example-card p {
    color: #bbbbbb;
    font-size: 14px;
    line-height: 1.6;
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
    line-height: 1.7;
}

.explain-box {
    background-color: #202020;
    border: 1px solid #393939;
    border-radius: 12px;
    padding: 25px;
    line-height: 1.8;
    margin-top: 15px;
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
    '<div class="sub-title">인공지능은 경사하강법을 어떻게 활용할까?</div>',
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
    "경사하강법은 인공지능이 학습하는 과정에서 예측 오차를 줄이는 데 "
    "활용되는 방법이다. 다양한 인공지능 기술의 학습 과정에서 사용될 수 있다."
)

examples = [
    ("🖼️ 이미지 인식", "사진 속 사물이나 사람의 특징을 학습하고 이미지를 구별한다."),
    ("🎙️ 음성 인식", "사람의 음성을 분석하여 말한 내용을 문자로 변환한다."),
    ("🌐 기계 번역", "문장의 의미와 언어의 패턴을 학습하여 다른 언어로 번역한다."),
    ("💬 감정 분석", "댓글이나 게시글에 담긴 긍정적·부정적 감정을 분석한다."),
    ("🚗 자율주행", "주변 차량과 보행자, 도로 등의 정보를 인식하는 모델을 학습한다."),
    ("🎬 영상 추천", "사용자의 시청 기록과 선호도를 바탕으로 관심 있을 만한 영상을 예측한다.")
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

st.markdown("""
<div class="explain-box">
    <span class="highlight">이번에 자세히 살펴볼 사례</span><br><br>
    영상 플랫폼의 콘텐츠 추천 알고리즘이다.
    사용자의 시청 기록과 선호도를 바탕으로 영상을 추천하는 과정에서
    예측 오차를 줄이는 데 경사하강법이 활용될 수 있다.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 02. 콘텐츠 추천 과정
# -------------------------------
st.markdown(
    '<div class="section-number">02 / RECOMMENDATION</div>'
    '<div class="section-title">영상 추천 알고리즘은 어떻게 작동할까?</div>',
    unsafe_allow_html=True
)

st.write(
    "영상 플랫폼은 사용자가 어떤 영상을 시청했는지, "
    "어떤 영상에 좋아요를 눌렀는지 등의 정보를 활용한다. "
    "이를 바탕으로 사용자가 어떤 영상에 관심을 가질지 예측한다."
)

steps = [
    ("STEP 1. 사용자 정보 수집",
     "시청 기록, 좋아요, 시청 시간, 선호하는 영상 분야 등의 정보를 모은다."),
    ("STEP 2. 관심도 예측",
     "수집한 정보를 바탕으로 사용자가 특정 영상에 얼마나 관심을 가질지 예측한다."),
    ("STEP 3. 실제 반응과 비교",
     "예측한 결과를 실제 시청이나 클릭 등의 반응과 비교한다."),
    ("STEP 4. 예측 오차 확인",
     "예측과 실제 반응 사이에 차이가 얼마나 있는지 확인한다."),
    ("STEP 5. 모델 학습",
     "경사하강법 등을 활용하여 예측 오차가 줄어들도록 모델을 조정한다.")
]

for title, description in steps:
    st.markdown(f"""
    <div class="step-card">
        <b class="highlight">{title}</b>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# 03. 경사하강법 적용 과정
# -------------------------------
st.markdown(
    '<div class="section-number">03 / LEARNING PROCESS</div>'
    '<div class="section-title">추천 알고리즘에서 경사하강법은 어떤 역할을 할까?</div>',
    unsafe_allow_html=True
)

st.write(
    "추천 알고리즘이 처음부터 사용자의 관심사를 정확하게 예측하는 것은 아니다. "
    "처음에는 예측이 실제 반응과 다를 수 있으며, 이러한 차이를 줄이는 학습 과정이 필요하다."
)

st.markdown("""
<div class="explain-box">
    <b>예를 들어 볼까?</b><br><br>
    어떤 사용자가 특정 영상을 실제로 시청했다고 가정해 보자.<br>
    추천 모델은 이 사용자가 해당 영상에 관심을 가질 가능성을 예측한다.<br><br>
    처음에는 예측 결과가 실제 반응과 다를 수 있다.
    이때 경사하강법을 이용해 모델의 설정값을 조금씩 조정하고,
    예측 오차를 줄이는 과정을 반복한다.<br><br>
    이러한 학습이 반복되면 모델은 사용자의 반응에서 패턴을 찾아
    관심 영상을 더 잘 예측할 수 있게 된다.
</div>
""", unsafe_allow_html=True)

st.markdown("#### 핵심 흐름")

st.markdown("""
<div class="step-card">
    <b>예측</b>
    <p>사용자가 어떤 영상에 관심을 가질지 예측한다.</p>
</div>
<div class="step-card">
    <b>비교</b>
    <p>예측 결과와 실제 반응을 비교하여 차이를 확인한다.</p>
</div>
<div class="step-card">
    <b>조정</b>
    <p>경사하강법을 활용하여 모델의 설정값을 조정한다.</p>
</div>
<div class="step-card">
    <b>반복 학습</b>
    <p>이 과정을 반복하면서 예측 오차를 줄여 나간다.</p>
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
    경사하강법을 여러 인공지능 기술의 활용 사례와 연결해 살펴보면서,
    수학에서 배우는 미분이 실제 인공지능의 학습 과정에도 활용된다는 점을 알게 되었다.
    특히 영상 추천 알고리즘은 사용자의 반응을 예측하고 그 오차를 줄이는 과정을
    반복한다는 점이 흥미로웠다. 처음에는 수학적인 계산 방법이라고만 생각했던
    경사하강법이 인공지능의 예측 성능을 개선하는 데 중요한 역할을 한다는 것을
    이해할 수 있었다.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 참고 자료
# -------------------------------
st.markdown("---")
st.markdown("### 참고 자료")

st.markdown("""
- Goodfellow et al., *Deep Learning*, Applications
- *Machine Learning: Algorithms, Real-World Applications and Research Directions*
- Microsoft Research, *Applications of Machine Learning*
""")

st.caption("※ 실제 추천 시스템은 서비스에 따라 사용하는 학습 방식과 알고리즘이 다를 수 있다.")
