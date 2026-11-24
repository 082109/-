
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

.explain-box {
    background-color: #202020;
    border: 1px solid #393939;
    border-radius: 12px;
    padding: 24px;
    line-height: 1.9;
    margin-top: 15px;
    margin-bottom: 20px;
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
    "예측 오차를 줄이는 데 활용된다. 대표적인 활용 사례를 살펴보자."
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
        "예측한 문장과 실제 문장의 차이를 줄이도록 학습한다."
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
# 02. 콘텐츠 추천 알고리즘
# -------------------------------
st.markdown(
    '<div class="section-number">02 / CONTENT RECOMMENDATION</div>'
    '<div class="section-title">영상 플랫폼에서는 어떻게 활용될까?</div>',
    unsafe_allow_html=True
)

st.write(
    "영상 플랫폼은 사용자의 행동 데이터를 분석해 "
    "어떤 콘텐츠에 관심을 가질지 예측한다. "
    "이 과정에서 경사하강법이 모델을 학습시키는 데 활용될 수 있다."
)

with st.container(border=True):
    st.subheader("① 사용자 데이터 수집")

    st.write(
        "플랫폼은 사용자가 어떤 영상을 시청했는지, "
        "얼마나 오래 시청했는지, 좋아요를 눌렀는지 등의 정보를 수집한다."
    )

    st.write(
        "이러한 정보는 인공지능이 학습할 수 있도록 숫자 형태의 데이터로 변환된다."
    )

    st.divider()

    st.subheader("② 관심도 예측")

    st.write(
        "인공지능은 사용자의 시청 기록과 영상의 특징을 바탕으로 "
        "특정 영상에 대한 관심도를 예측한다."
    )

    st.write(
        "예를 들어 사용자가 과학 실험 영상을 자주 시청했다면, "
        "새로운 과학 영상에도 관심을 가질 가능성이 있다고 예측할 수 있다."
    )

    st.divider()

    st.subheader("③ 실제 반응과 비교")

    st.write(
        "모델이 예측한 관심도와 사용자의 실제 반응을 비교한다. "
        "예측이 실제 반응과 다르다면 그 차이를 줄이는 학습이 필요하다."
    )


# -------------------------------
# 수학적 예시
# -------------------------------
st.markdown("### 숫자로 이해하는 예측 오차")

st.write(
    "이해를 돕기 위해 관심도 예측값을 0과 1 사이의 숫자로 나타내는 "
    "간단한 예시를 살펴보자."
)

with st.container(border=True):
    st.markdown("#### 상황")

    st.write(
        "인공지능이 어떤 영상에 대한 사용자의 관심도를 0.3으로 예측했다. "
        "그런데 사용자는 실제로 해당 영상을 시청했다."
    )

    st.markdown("#### 예측값과 실제 반응")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("인공지능의 예측값", "0.3")

    with col2:
        st.metric("실제 반응값", "1.0")

    st.write("두 값의 차이를 제곱하여 오차를 계산하는 간단한 예시를 사용하면,")

    st.latex(r"L=(\text{실제값}-\text{예측값})^2")

    st.latex(r"L=(1-0.3)^2=0.49")

    st.markdown(
        '<p class="highlight">계산된 오차는 0.49이다.</p>',
        unsafe_allow_html=True
    )

    st.write(
        "이처럼 인공지능은 예측값과 실제 반응의 차이를 수치로 계산할 수 있다. "
        "실제 추천 시스템에서는 예측 문제의 종류에 따라 다른 오차 계산 방법도 사용한다."
    )


# -------------------------------
# 03. 경사하강법의 적용
# -------------------------------
st.markdown(
    '<div class="section-number">03 / GRADIENT DESCENT</div>'
    '<div class="section-title">경사하강법은 이 오차를 어떻게 줄일까?</div>',
    unsafe_allow_html=True
)

st.write(
    "오차를 계산했다면 다음 단계는 오차가 작아지도록 "
    "인공지능 모델의 설정값을 조정하는 것이다."
)

with st.container(border=True):
    st.subheader("① 모델의 설정값 확인")

    st.write(
        "인공지능 모델에는 예측 결과에 영향을 주는 여러 설정값이 있다. "
        "이 값들을 조정하면 모델의 예측 결과도 달라진다."
    )

    st.divider()

    st.subheader("② 미분값을 이용한 방향 확인")

    st.write(
        "손실함수를 미분하면 모델의 설정값이 변할 때 "
        "오차가 어느 방향으로 변하는지 알 수 있다. "
        "경사하강법은 이 미분값을 이용해 오차가 작아지는 방향을 찾는다."
    )

    st.latex(r"w_{\text{새로운 값}}=w_{\text{기존 값}}-\eta L'(w)")

    st.write(
        "여기서 w는 모델의 설정값, η는 학습률, "
        "L'(w)는 설정값에 따른 손실함수의 미분값을 의미한다."
    )

    st.divider()

    st.subheader("③ 설정값 조정과 반복 학습")

    st.write(
        "미분값과 학습률을 이용해 설정값을 조금씩 바꾸고, "
        "다시 예측 오차를 계산한다. "
        "이 과정을 반복하면서 오차가 줄어들도록 모델을 학습시킨다."
    )


# -------------------------------
# 학습 과정의 변화
# -------------------------------
st.markdown("### 반복 학습을 통해 달라지는 점")

with st.container(border=True):
    st.subheader("학습 전")

    st.write(
        "사용자의 시청 기록을 바탕으로 관심 콘텐츠를 예측하지만 "
        "실제 반응과 차이가 클 수 있다."
    )

    st.divider()

    st.subheader("학습 과정")

    st.write(
        "예측 오차를 계산하고 미분값을 이용해 모델의 설정값을 조정한다. "
        "이 과정을 여러 번 반복한다."
    )

    st.divider()

    st.subheader("학습 후")

    st.write(
        "반복 학습을 통해 사용자의 반응에서 패턴을 찾아내고, "
        "관심 콘텐츠를 더 정확하게 예측할 수 있도록 모델이 개선된다."
    )


# -------------------------------
# 핵심 정리
# -------------------------------
with st.container(border=True):
    st.markdown(
        '<p class="highlight">핵심 정리</p>',
        unsafe_allow_html=True
    )

    st.write(
        "영상 플랫폼의 콘텐츠 추천 모델은 사용자의 행동 데이터를 바탕으로 "
        "관심도를 예측한다. 이때 예측 오차를 계산하고, "
        "미분값을 이용해 모델의 설정값을 조정하는 과정에 "
        "경사하강법이 활용될 수 있다."
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
        "특히 평소 자주 사용하는 영상 플랫폼의 추천 기능을 사례로 살펴보면서, "
        "사용자의 행동을 숫자로 나타내고 예측 오차를 계산한 뒤 "
        "미분을 통해 모델의 설정값을 조정한다는 점이 흥미로웠다. "
        "수학 시간에 배운 미분이 단순한 계산을 넘어 "
        "인공지능이 스스로 학습하고 예측 성능을 개선하는 과정에 "
        "활용된다는 것을 구체적으로 이해할 수 있었다."
    )
