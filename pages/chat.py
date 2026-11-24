
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
# 02. 영상 플랫폼 활용 과정
# -------------------------------
st.markdown(
    '<div class="section-number">02 / CONTENT RECOMMENDATION</div>'
    '<div class="section-title">영상 플랫폼에서는 어떻게 활용될까?</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div style="
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    background-color: #202020;
    border: 1px solid #393939;
    border-radius: 14px;
    padding: 35px 20px;
    flex-wrap: wrap;
">
    <div style="font-size: 21px; font-weight: bold;">
        ① 사용자 데이터 수집
    </div>

    <div style="color: #ff625e; font-size: 28px;">
        →
    </div>

    <div style="font-size: 21px; font-weight: bold;">
        ② 관심도 예측
    </div>

    <div style="color: #ff625e; font-size: 28px;">
        →
    </div>

    <div style="font-size: 21px; font-weight: bold;">
        ③ 실제 반응과 비교
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------------------
# 숫자로 이해하는 예측 오차
# -------------------------------
st.markdown(
    '<div class="section-number">03 / PREDICTION ERROR</div>'
    '<div class="section-title">숫자로 이해하는 예측 오차</div>',
    unsafe_allow_html=True
)

st.write(
    "이해를 돕기 위해 관심도 예측값을 0과 1 사이의 숫자로 나타내는 "
    "간단한 예시를 살펴보자."
)

with st.container(border=True):
    st.subheader("상황")

    st.write(
        "인공지능이 어떤 영상에 대한 사용자의 관심도를 0.3으로 예측했다. "
        "그런데 사용자는 실제로 해당 영상을 시청했다."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("인공지능의 예측값", "0.3")

    with col2:
        st.metric("실제 반응값", "1.0")

    st.divider()

    st.subheader("① 두 값의 차이 계산")

    st.write(
        "먼저 실제 반응값에서 예측값을 빼면 두 값의 차이를 구할 수 있다."
    )

    st.latex(r"1-0.3=0.7")

    st.subheader("② 왜 차이를 제곱할까?")

    st.write(
        "오차를 단순히 빼기만 하면 음수와 양수가 나타날 수 있다. "
        "여러 오차를 합칠 때 서로 상쇄되는 문제를 막기 위해 "
        "제곱하는 방법을 사용할 수 있다."
    )

    st.write(
        "또한 오차가 클수록 제곱한 값이 더 커지기 때문에 "
        "큰 오차를 더욱 크게 반영할 수 있다."
    )

    st.latex(r"L=(\text{실제값}-\text{예측값})^2")

    st.latex(r"L=(1-0.3)^2=0.49")

    st.markdown(
        '<p class="highlight">계산된 손실값은 0.49이다.</p>',
        unsafe_allow_html=True
    )

    st.write(
        "이처럼 예측값과 실제 반응값의 차이를 수치로 나타내는 함수를 "
        "손실함수라고 한다. 여기서는 이해를 위해 제곱 오차를 사용했다."
    )

    st.caption(
        "실제 추천 시스템에서는 문제의 종류에 따라 다른 손실함수를 사용하기도 한다."
    )


# -------------------------------
# 04. 경사하강법의 수학적 원리
# -------------------------------
st.markdown(
    '<div class="section-number">04 / GRADIENT DESCENT</div>'
    '<div class="section-title">경사하강법은 이 오차를 어떻게 줄일까?</div>',
    unsafe_allow_html=True
)

st.write(
    "오차를 계산했다면 다음 단계는 오차가 작아지도록 "
    "인공지능 모델의 설정값을 조정하는 것이다. "
    "이때 미분이 사용된다."
)

# ① 손실함수 미분
with st.container(border=True):
    st.subheader("① 손실함수를 미분하기")

    st.write(
        "모델의 설정값에 따라 손실값이 어떻게 달라지는지 알아보기 위해 "
        "손실함수를 미분한다."
    )

    st.write(
        "이해를 돕기 위해 모델의 설정값을 w라고 하고, "
        "이 간단한 예시에서는 w가 예측값을 나타낸다고 생각해 보자."
    )

    st.latex(r"L(w)=(1-w)^2")

    st.write(
        "실제 반응값은 1이고, 현재 예측값은 0.3이므로 "
        "w에 0.3을 대입한 것이다."
    )

    st.write("이 함수를 미분하면 다음과 같다.")

    st.latex(r"L'(w)=2(w-1)")

    st.write("여기에 현재 값인 w=0.3을 대입하면,")

    st.latex(r"L'(0.3)=2(0.3-1)=-1.4")

    st.markdown(
        '<p class="highlight">미분값은 -1.4이다.</p>',
        unsafe_allow_html=True
    )

    st.write(
        "미분값이 음수라는 것은 현재 설정값을 증가시키는 방향으로 "
        "이동하면 손실값이 감소할 수 있다는 뜻이다."
    )


# ② 이동 방향 확인
with st.container(border=True):
    st.subheader("② 미분값으로 이동 방향 확인하기")

    st.write(
        "미분값의 부호를 통해 손실값이 작아지는 방향을 판단할 수 있다."
    )

    st.markdown("""
    - 미분값이 양수라면 설정값을 줄이는 방향으로 이동한다.
    - 미분값이 음수라면 설정값을 늘리는 방향으로 이동한다.
    """)

    st.write(
        "따라서 앞의 예시처럼 미분값이 -1.4라면 "
        "설정값을 증가시키는 방향으로 조정해야 한다."
    )


# ③ 학습률을 이용한 조정
with st.container(border=True):
    st.subheader("③ 학습률을 이용해 설정값 조정하기")

    st.write(
        "설정값을 얼마나 바꿀지는 학습률에 따라 달라진다. "
        "학습률은 한 번에 이동하는 크기를 조절하는 값이다."
    )

    st.write(
        "경사하강법의 설정값 조정 과정을 식으로 나타내면 다음과 같다."
    )

    st.latex(
        r"\text{새로운 값}"
        r"=\text{기존 값}-\text{학습률}\times\text{미분값}"
    )

    st.write(
        "앞의 예시에서 학습률을 0.1이라고 가정해 보자."
    )

    st.latex(r"w_{\text{새로운 값}}=0.3-0.1\times(-1.4)")

    st.latex(r"w_{\text{새로운 값}}=0.44")

    st.markdown(
        '<p class="highlight">설정값이 0.3에서 0.44로 바뀌었다.</p>',
        unsafe_allow_html=True
    )

    st.write(
        "미분값이 음수였기 때문에 마이너스와 음수가 만나 "
        "설정값이 증가한 것이다. "
        "이처럼 미분값의 반대 방향으로 이동해 "
        "오차가 작아지는 방향을 찾는다."
    )


# ④ 반복 학습
with st.container(border=True):
    st.subheader("④ 다시 오차를 계산하고 반복하기")

    st.write(
        "설정값이 0.44로 바뀌었으므로 예측값도 0.44가 되었다고 생각해 보자. "
        "이때 새로운 손실값을 계산하면 다음과 같다."
    )

    st.latex(r"L=(1-0.44)^2=0.3136")

    st.write(
        "처음 손실값은 0.49였지만, 설정값을 조정한 후에는 0.3136으로 줄어들었다."
    )

    st.markdown(
        '<p class="highlight">0.49 → 0.3136으로 손실값이 감소했다!</p>',
        unsafe_allow_html=True
    )

    st.write(
        "실제 학습에서는 이처럼 설정값을 조정하고 손실값을 다시 계산하는 과정을 "
        "여러 번 반복한다. 이를 통해 모델의 예측 오차를 줄여 나간다."
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
        "경사하강법은 손실함수를 미분해 오차가 작아지는 방향을 찾고, "
        "학습률을 이용해 모델의 설정값을 조금씩 조정하는 방법이다. "
        "이 과정을 반복하면서 인공지능 모델의 예측 성능을 개선한다."
    )


# -------------------------------
# 05. 느낀점
# -------------------------------
st.markdown(
    '<div class="section-number">05 / REFLECTION</div>'
    '<div class="section-title">느낀점</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.write(
        "경사하강법이 이미지 인식, 음성 인식, 콘텐츠 추천 등 "
        "다양한 인공지능 기술의 학습 과정에 활용된다는 점을 알게 되었다. "
        "특히 영상 플랫폼의 콘텐츠 추천 과정을 수학적으로 살펴보면서, "
        "예측값과 실제 반응의 차이를 손실함수로 나타내고 "
        "이를 미분해 설정값을 조정한다는 점을 이해할 수 있었다. "
        "수학 시간에 배운 미분이 단순한 계산을 넘어 "
        "인공지능이 스스로 학습하고 예측 결과를 개선하는 과정에 "
        "활용된다는 점이 인상 깊었다."
    )
