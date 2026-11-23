
import streamlit as st

# ==========================================
# 1. 페이지 설정
# ==========================================

st.set_page_config(
    page_title="Gradient Descent",
    page_icon="📉",
    layout="wide"
)

# ==========================================
# 2. 디자인
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #101010;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    color: white !important;
}

p, li {
    color: #dddddd;
    line-height: 1.9;
    font-size: 16px;
}

.main-title {
    font-size: 48px;
    font-weight: 900;
    letter-spacing: -2px;
    color: white;
}

.sub-title {
    font-size: 17px;
    color: #aaaaaa;
    margin-top: 10px;
}

.page-number {
    color: #ff5555;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 3px;
}

.slide-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 12px;
    margin-bottom: 20px;
}

.card {
    background-color: #202020;
    border: 1px solid #383838;
    border-radius: 14px;
    padding: 23px;
    height: 100%;
}

.card-title {
    color: #ff5555;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 12px;
}

.big-text {
    font-size: 23px;
    font-weight: bold;
    line-height: 1.6;
    color: white;
}

.highlight {
    color: #ff5555;
    font-weight: bold;
}

.formula-box {
    background-color: #202020;
    border: 1px solid #ff5555;
    border-radius: 14px;
    padding: 25px;
    text-align: center;
}

.small-text {
    color: #aaaaaa;
    font-size: 14px;
}

hr {
    border-color: #383838;
    margin-top: 35px;
    margin-bottom: 35px;
}

div[data-testid="stProgress"] > div > div {
    background-color: #ff5555;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. 상단 제목
# ==========================================

st.markdown(
    '<div class="main-title">GRADIENT DESCENT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">미분으로 이해하는 인공지능의 최적화 원리</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ==========================================
# 4. 목차
# ==========================================

st.markdown("### CONTENTS")

contents = [
    "경사하강법이란?",
    "최적화와 인공지능",
    "손실함수",
    "미분의 역할",
    "미분값과 학습률",
    "경사하강법의 수식"
]

cols = st.columns(3)

for i, content in enumerate(contents):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <span class="highlight">0{i+1}</span>
            <p><b>{content}</b></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 01. 경사하강법이란?
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 01 / INTRODUCTION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">경사하강법이란?</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="formula-box">
    <div class="big-text">
        미분을 활용하여 함수의 최솟값을 찾아가는<br>
        최적화 알고리즘
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

st.write("""
경사하강법(Gradient Descent)은 함수의 값이 작아지는 방향으로
현재 값을 조금씩 수정하면서 최솟값을 찾아가는 방법이다.

현재 위치에서 함수가 어떻게 변하는지 확인하고,
그 정보를 바탕으로 다음 위치를 결정한다.
이 과정을 반복하면서 점점 최솟값에 가까워진다.
""")

st.markdown("""
<div class="card">
    <div class="card-title">핵심 원리</div>
    <p class="big-text">
        현재 위치 확인 → 미분값 계산 → 이동 방향 결정
        → 다음 위치로 이동 → 반복
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 02. 최적화와 인공지능
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 02 / OPTIMIZATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">최적화와 인공지능</div>',
    unsafe_allow_html=True
)

st.write("""
최적화란 주어진 조건에서 함수의 값이 최대 또는 최소가 되는
상태를 찾아내는 과정이다.

인공지능 모델도 학습 과정에서 최적화를 활용한다.
모델이 예측한 결과와 실제 결과 사이의 오차를 줄이기 위해
내부의 여러 값을 반복적으로 조정하는 것이다.
""")

st.subheader("인공지능은 무엇을 조정할까?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">WEIGHT / 가중치</div>
        <p class="big-text">입력 정보의 영향력</p>
        <p>
        입력된 정보가 예측 결과에 얼마나 큰 영향을 미칠지
        결정하는 값이다.
        </p>
        <p class="small-text">
        예: 특정 정보가 예측 결과에 더 중요하게 반영되도록 조정
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">BIAS / 편향</div>
        <p class="big-text">예측 결과의 추가 조정</p>
        <p>
        가중치와 입력값으로 계산한 결과에 추가되는 값으로,
        모델의 예측 결과를 조정하는 역할을 한다.
        </p>
        <p class="small-text">
        예: 예측 결과가 적절한 위치에 오도록 조정
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("""
인공지능은 학습하면서 가중치와 편향을 조금씩 수정한다.
이러한 값이 달라지면 예측 결과도 달라지고,
결과적으로 실제값과의 오차도 달라진다.
""")

st.markdown("""
<div class="card">
    <div class="card-title">REMEMBER</div>
    <p>
    가중치와 편향은 인공지능 모델이 학습하면서 조정하는 값이다.
    경사하강법은 이러한 값을 수정하여 손실함수를 최소화하는 데 활용된다.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 03. 손실함수
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 03 / LOSS FUNCTION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">손실함수란 무엇일까?</div>',
    unsafe_allow_html=True
)

st.write("""
인공지능이 예측한 값이 항상 실제 결과와 일치하는 것은 아니다.
예측값과 실제값 사이에는 오차가 발생할 수 있다.

손실함수(Loss Function)는 이러한 오차를 수학적으로 나타내는 함수이다.
일반적으로 손실함수의 값이 작을수록 모델의 예측 오차가 작다는 의미이다.
""")

st.latex(r"J(\theta)")

st.markdown("""
<div class="card">
    <div class="card-title">LOSS FUNCTION</div>
    <p class="big-text">손실함수 = 예측 오차를 나타내는 함수</p>
    <p>
    인공지능은 손실함수의 값을 줄이는 방향으로 학습한다.
    이를 위해 가중치와 편향을 계속 조정한다.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.subheader("간단한 예시")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">PREDICTION</div>
        <p class="big-text">예측값 4점</p>
        <p>인공지능이 예상한 이용자의 선호도</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">ACTUAL VALUE</div>
        <p class="big-text">실제값 2점</p>
        <p>실제 이용자가 보인 선호도</p>
    </div>
    """, unsafe_allow_html=True)

st.write("""
예측값은 4점이지만 실제값은 2점이므로 오차가 발생한다.
인공지능은 이러한 오차를 줄이기 위해 모델을 학습한다.
""")

st.markdown("""
<div class="formula-box">
    <div class="card-title">IMPORTANT QUESTION</div>
    <div class="big-text">
        그렇다면 손실함수의 값이<br>
        어느 방향으로 감소하는지 어떻게 알 수 있을까?
    </div>
    <p class="highlight">바로 미분을 활용한다!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 04. 미분의 역할
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 04 / DERIVATIVE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">미분은 왜 필요할까?</div>',
    unsafe_allow_html=True
)

st.write("""
미분은 특정 위치에서 함수의 순간변화율을 구하는 방법이다.

순간변화율은 현재 위치에서 x값이 아주 조금 변할 때
함수값이 얼마나 빠르게 변하는지를 나타낸다.

그래프에서는 특정 위치에 그은 접선의 기울기로 이해할 수 있다.
""")

st.latex(r"f'(x)=\text{순간변화율}")

st.subheader("미분값으로 이동 방향 판단하기")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">기울기가 양수 (+)</div>
        <p class="big-text">↙ 왼쪽으로 이동</p>
        <p>
        현재 위치에서 오른쪽으로 갈수록 함수값이 커지는 상황이다.
        따라서 함수값을 줄이려면 왼쪽으로 이동해야 한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">기울기가 음수 (-)</div>
        <p class="big-text">오른쪽으로 이동 ↘</p>
        <p>
        현재 위치에서 오른쪽으로 갈수록 함수값이 작아지는 상황이다.
        따라서 오른쪽으로 이동해야 한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("""
<div class="card">
    <div class="card-title">기울기가 0이라면?</div>
    <p>
    접선이 수평이라는 의미이다. 다만 미분값이 0이라고 해서
    항상 최솟값인 것은 아니다. 최댓값이나 다른 정지점일 수도 있다.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 05. 미분값과 학습률
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 05 / LEARNING RATE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">미분값과 학습률의 역할</div>',
    unsafe_allow_html=True
)

st.write("""
미분을 통해 함수값이 감소하는 방향을 알았다면,
이제 그 방향으로 얼마나 이동할지 결정해야 한다.

이때 사용하는 값이 학습률(Learning Rate)이다.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">미분값 / DERIVATIVE</div>
        <p class="big-text">어느 방향으로?</p>
        <p>
        현재 위치에서 함수가 변하는 방향과 정도를 알려 준다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">학습률 / LEARNING RATE</div>
        <p class="big-text">얼마나 이동할까?</p>
        <p>
        한 번의 계산에서 값을 얼마나 크게 수정할지 결정한다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("학습률에 따른 차이")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">너무 작을 때</div>
        <p class="big-text">조금씩 이동</p>
        <p>최솟값에 도달하기까지 많은 반복이 필요할 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">적절할 때</div>
        <p class="big-text">안정적 이동</p>
        <p>최솟값에 효율적으로 가까워질 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">너무 클 때</div>
        <p class="big-text">지나칠 수 있음</p>
        <p>최솟값을 지나쳐 오히려 멀어질 수 있다.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 06. 경사하강법의 수식
# ==========================================

st.markdown(
    '<div class="page-number">PAGE 06 / GRADIENT DESCENT FORMULA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="slide-title">경사하강법의 수식</div>',
    unsafe_allow_html=True
)

st.write("""
지금까지 알아본 미분값과 학습률을 이용하면
다음 위치를 계산할 수 있다.
""")

st.markdown("""
<div class="formula-box">
    <div class="card-title">GRADIENT DESCENT</div>
</div>
""", unsafe_allow_html=True)

st.latex(r"x_{t+1}=x_t-\alpha f'(x_t)")

st.subheader("수식 속 기호의 의미")

symbols = [
    ("xₜ", "현재 위치", "현재 함수에서의 x값"),
    ("xₜ₊₁", "다음 위치", "현재 값을 수정한 뒤 새롭게 정해지는 x값"),
    ("f'(xₜ)", "미분값", "현재 위치에서의 순간변화율"),
    ("α", "학습률", "한 번에 얼마나 이동할지 결정하는 값")
]

for symbol, name, description in symbols:
    st.markdown(f"""
    <div class="card">
        <span class="highlight">{symbol}</span>
        <p class="big-text">{name}</p>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("왜 미분값을 빼는 것일까?")

st.write("""
경사하강법은 현재 위치에서 함수값이 감소하는 방향으로 이동해야 한다.

미분값이 양수라면 양수를 빼기 때문에 x값이 작아진다.
미분값이 음수라면 음수를 빼기 때문에 x값이 커진다.

결국 미분값의 반대 방향으로 이동하도록 수식이 만들어진 것이다.
""")

st.markdown("""
<div class="formula-box">
    <div class="card-title">핵심 정리</div>
    <div class="big-text">
        미분으로 이동 방향을 판단하고,<br>
        학습률로 이동 크기를 조절한다.
    </div>
    <p class="highlight">
        이 과정을 반복하여 함수의 최솟값을 찾아가는 것이 경사하강법이다.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================
# 마무리
# ==========================================

st.markdown("### FINAL SUMMARY")
st.header("경사하강법, 핵심만 기억하기")

summary = [
    ("최적화", "함수의 최댓값 또는 최솟값을 찾는 과정"),
    ("손실함수", "인공지능의 예측 오차를 나타내는 함수"),
    ("미분", "현재 위치에서 함수의 순간변화율을 구하는 방법"),
    ("학습률", "한 번에 값을 얼마나 수정할지 결정하는 값"),
    ("경사하강법", "미분을 활용해 손실함수를 최소화하는 최적화 알고리즘")
]

for title, description in summary:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.success("다음 단계에서는 직접 그래프를 조절하며 경사하강법의 작동 과정을 확인해 볼 수 있어!")
